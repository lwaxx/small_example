// step1: 在 components 中创建一个 treeSelect 文件夹，里面创建一个 index.vue 文件。里面的代码可以直接复制粘贴
<template>
  <el-select
    class="tree-select"
    ref="treeSelect"
    @visible-change="onPopperVisibleChange"
    v-model="selectedValue"
    :multiple="multiple"
    :disabled="disabled"
    :size="size"
    :clearable="clearable"
    :popper-class="multiple ? 'tree-select multi-select-tree' : 'tree-select single-select-tree'"
    :collapse-tags="collapseTags"
    :name="name"
    :placeholder="placeholder"
    @remove-tag="onRemoveItem"
  >
    <el-option
      v-for="item in listData"
      :key="item[nodeKey]"
      :label="item[props.label || 'label']"
      :value="item[nodeKey]"
    ></el-option>
  </el-select>
</template>

<script>
  import Vue from "vue";

  function getNodes(node, temp) {
    temp.push(node);
    if (Array.isArray(node.children)) {
      node.children.forEach(item => {
        getNodes(item, temp);
      });
    }
  }

  export default {
    name: "ElTreeSelect",
    props: {
      value: {
        type: [String, Number, Array]
      },
      multiple: {
        type: Boolean,
        default: false
      },
      disabled: {
        type: Boolean,
        default: false
      },
      size: {
        type: String,
        default: "default"
      },
      clearable: {
        type: Boolean,
        default: false
      },
      collapseTags: {
        type: Boolean,
        default: true
      },
      name: {
        type: String
      },
      placeholder: {
        type: String
      },
      data: {
        type: Array
      },
      nodeKey: {
        type: String,
        required: true
      },
      props: {
        type: Object,
        default: function() {
          return {
            label: "label",
            children: "children",
            disabled: "disabled"
          };
        }
      },
      defaultExpandAll: {
        type: Boolean,
        default: true
      },
      expandOnClickNode: {
        type: Boolean,
        default: false
      },
      checkOnClickNode: {
        type: Boolean,
        default: true
      },
      checkStrictly: {
        type: Boolean,
        default: true
      },
      accordion: {
        type: Boolean,
        default: false
      }
    },
    data() {
      return {
        selectedValue: this.value,
        dropdownTree: null,
        listData: []
      };
    },
    methods: {
      onPopperVisibleChange(isVisible) {
        if (isVisible) {
          this.$nextTick(() => {
            let dom = document.createElement("div");
            let items = document.getElementsByClassName(
              "el-select-dropdown__item"
            );
            for (let i = 0; i < items.length; i++) {
              items[i].style.display = "none";
            }
            let dorpdownList = document.getElementsByClassName(
              "tree-select el-select-dropdown"
            );
            let dropdownItem = dorpdownList[dorpdownList.length - 1];
            dropdownItem
              .getElementsByClassName("el-select-dropdown__list")[0]
              .appendChild(dom);
            let Tree = Vue.component("ElTree");
            this.dropdownTree = new Tree({
              propsData: {
                ...this.treeProps
              }
            });
            this.dropdownTree.$on("current-change", (data, node) => {
              if (!this.multiple) {
                this.selectedValue = data.deptId;
                this.$refs.treeSelect.blur();
              }
            });
            this.dropdownTree.$mount(dom);
            if (!this.multiple && this.selectedValue != null) {
              setTimeout(() => {
                this.dropdownTree.setCurrentKey(this.selectedValue);
              });
            }
          });
        } else {
          let temp;
          if (this.multiple) {
            temp = this.dropdownTree.getCheckedKeys();
          } else {
            temp = this.dropdownTree.getCurrentKey();
          }
          this.dropdownTree = null;
          let dorpdownList = document.getElementsByClassName(
            "tree-select el-select-dropdown"
          );
          let dropdownItem = dorpdownList[dorpdownList.length - 1];
          let parent = dropdownItem.getElementsByClassName(
            "el-select-dropdown__list"
          )[0];
          let treeNode = parent.getElementsByClassName("el-tree")[0];
          parent.removeChild(treeNode);
          this.selectedValue = temp;
          this.$nextTick(() => {
            let items = document.getElementsByClassName(
              "el-select-dropdown__item"
            );
            for (let i = 0; i < items.length; i++) {
              items[i].style.display = "block";
            }
          });
        }
      },
      onRemoveItem(tagValue) {
        if (this.dropdownTree != null) {
          let checkedKeys = this.dropdownTree.getCheckedKeys();
          if (checkedKeys.indexOf(tagValue) !== -1) {
            this.dropdownTree.setCheckedKeys(
              checkedKeys.filter(item => {
                return item !== tagValue;
              })
            );
          }
        } else {
          this.$emit("remove-tag", tagValue);
        }
      },
      getListData() {
        this.listData = [];
        if (Array.isArray(this.data)) {
          this.data.forEach(item => {
            getNodes(item, this.listData);
          });
        }
      }
    },
    computed: {
      treeProps() {
        return {
          data: this.data,
          nodeKey: this.nodeKey,
          defaultExpandAll: this.defaultExpandAll,
          expandOnClickNode: this.expandOnClickNode,
          checkOnClickNode: this.checkOnClickNode,
          checkStrictly: this.checkStrictly,
          accordion: this.accordion,
          props: this.props,
          showCheckbox: this.multiple,
          defaultCheckedKeys: this.multiple ? this.selectedValue : undefined,
          highlightCurrent: !this.multiple
        };
      }
    },
    watch: {
      data: {
        handler: function(newVal, oldVal) {
          this.getListData();
        },
        immediate: true,
        deep: true
      },
      value: {
        handler: function(newVal, oldVal) {
          this.selectedValue = newVal;
        },
        immediate: true,
        deep: true
      },
      selectedValue: {
        handler: function(newVal, oldVal) {
          if (
            JSON.stringify(newVal) !== JSON.stringify(oldVal) &&
            this.dropdownTree == null
          ) {
            this.$emit("input", newVal);
            this.$emit("change", newVal);
          }
        }
      }
    }
  };
</script>

<style lang="scss">
  .tree-select {
    .el-tree-node__content {
      height: 34px;
      line-height: 34px;
      padding-right: 10px;
    }
  }

  .tree-select.single-select-tree {
    .el-tree-node.is-current > .el-tree-node__content > .el-tree-node__label {
      color: #409eff;
      font-weight: 700;
    }
  }
</style>


// step2: 在需要的地方引入
import ElTreeSelect from "@/components/treeSelect/index.vue"; // 树形选择器组件
components: {
      ElTreeSelect
    }
    单选版//
<el-tree-select
   style="width:100%"
   :data="treeData"
   v-model="formInline.level"
   node-key="id"
/>
多选版//
   <el-tree-select
      :data="treeData"
      v-model="value2"
      node-key="id"
      size="mini"
      :multiple="true"
    />


// step3: 最后一步
return中
 value1: undefined,
        value2: [],
        value3: [],
        treeData: [
          {
            id: 0,
            label: "运营系统",
            children: [
              {
                id: 10,
                label: "运营数据统计",
                children: [
                  {
                    id: 11,
                    label: "平台综合统计"
                  },
                  {
                    id: 12,
                    label: "各游戏综合统计"
                  },
                  {
                    id: 13,
                    label: "各房间综合统计"
                  },
                  {
                    id: 14,
                    label: "留存综合数据统计"
                  }
                ]
              },
              {
                id: 15,
                label: "在线数据统计",
                children: [
                  {
                    id: 16,
                    label: "最高在线数据统计"
                  },
                  {
                    id: 17,
                    label: "同时在线统计"
                  }
                ]
              }
            ]
          }
        ]
