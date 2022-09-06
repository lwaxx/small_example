package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"os"
	"path"
	"runtime"
	"sync"
)

type EggBox struct {
	Percent int   `json:"p"` // 占百分比
	Coin    int64 `json:"c"` // 给送礼者返钻
	GiftNum int64 `json:"n"` // 礼物个数
	GiftID  int64 `json:"i"` // 礼物id
}

type EggResult struct {
	EggItems []*EggBox `json:"item_list"`
}

type eggConfigLIst struct {
	Items []*EggBox
	sync.RWMutex
}

var eggs = eggConfigLIst{Items: make([]*EggBox, 0)}

var EGG_CONFIG_STR string

func loadEggConfig(fileName string) eggConfigLIst {
	f, err := os.Open(fileName)
	if err != nil {
		fmt.Printf("err: %v\n", err)
	}
	eggJson, err := ioutil.ReadAll(f)
	if err != nil {
		fmt.Printf("err: %v\n", err)
	}
	f.Close()
	if string(eggJson) == EGG_CONFIG_STR {
		// return
		fmt.Printf("err: %v\n", err)
	}
	EGG_CONFIG_STR = string(eggJson)

	var res EggResult
	err = json.Unmarshal(eggJson, &res)
	if err != nil {
		fmt.Printf("err: %v\n", err)
	}

	eggs.Lock()
	eggs.Items = make([]*EggBox, 0)
	for _, e := range res.EggItems {
		eggs.Items = append(eggs.Items, e)
	}
	eggs.Unlock()

	for i := 0; i < len(eggs.Items); i++ {
		fmt.Printf("eggs info: %v\n", *(eggs.Items[i]))
	}
	fmt.Printf("eggs: %v\n", eggs.Items)
	return eggs
}

func Get_Eggs_Arr(arr []*EggBox) map[int64]int64 {
	if arr == nil {
		return nil
	}
	len1 := len(arr)
	if len1 == 0 {
		return nil
	}
	m := make(map[int64]int64, 0)
	for _, v := range arr {
		if v == nil {
			continue
		}
		rwd_type := v.GiftID
		rwd_num := v.GiftNum
		m[rwd_type] += rwd_num
	}
	return m
}

func Get_Eggs_Arr_Struct(arr *eggConfigLIst) map[int64]int64 {
	if arr == nil {
		return nil
	}
	len1 := len(arr.Items)
	if len1 == 0 {
		return nil
	}
	m := make(map[int64]int64, 0)
	for _, v := range arr.Items {
		if v == nil {
			continue
		}
		rwd_type := v.GiftID
		rwd_num := v.GiftNum
		m[rwd_type] += rwd_num
	}
	return m
}

// 获取当前执行程序所在的绝对路径
func getCurrentAbPathByCaller() string {
	var abPath string
	_, filename, _, ok := runtime.Caller(0)
	if ok {
		abPath = path.Dir(filename)
	}
	return abPath
}

// --------- omitempty参数详解 start --------------
type address struct {
	Street  string `json:"street"`  // 街道
	Ste     string `json:"suite"`   // 单元（可以不存在）
	City    string `json:"city"`    // 城市
	State   string `json:"state"`   // 州/省
	Zipcode string `json:"zipcode"` // 邮编
}

type addressOmi struct {
	Street  string `json:"street"`
	Ste     string `json:"suite,omitempty"`
	City    string `json:"city"`
	State   string `json:"state"`
	Zipcode string `json:"zipcode"`
}

// --------- omitempty参数详解 end --------------

func main() {
	// 获取当前路径
	// path := getCurrentAbPathByCaller()
	// fmt.Println(path)

	// 结构体赋值
	eggs := loadEggConfig("/Users/liwei/Desktop/others/test111111111111111/go测试/EggBoxConfig.json")
	fmt.Println(eggs)
	fmt.Println("-----------------")

	// 数组指针传参
	res := Get_Eggs_Arr(eggs.Items)
	fmt.Println(res)
	fmt.Println("-----------------")

	// 结构体传参
	res_struct := Get_Eggs_Arr_Struct(&eggs)
	fmt.Println(res_struct)
	fmt.Println("-----------------")

	// omitempty参数详解
	data := `{
		"street": "200 Larkin St",
		"city": "San Francisco",
		"state": "CA",
		"zipcode": "94102"
	}`
	addr := new(address)
	json.Unmarshal([]byte(data), &addr)
	addressBytes, _ := json.MarshalIndent(addr, "", "    ")
	fmt.Printf("%s\n", string(addressBytes))

	// 加上omitempty后，json序列化之后，如果没有该字段，就不会显示
	addrOmi := new(addressOmi)
	json.Unmarshal([]byte(data), &addrOmi)
	addressBytesOmi, _ := json.MarshalIndent(addrOmi, "", "    ")
	fmt.Printf("%s\n", string(addressBytesOmi))

}
