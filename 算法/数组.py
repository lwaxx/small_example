# 实现数组的插入与删除

class MyArray:
    def __init__(self, capacity):
        self.array = [None] * capacity
        self.size = 0

    def insert(self, index, element):
        """不用扩容的情况"""
        # 判断访问下标是否超出范围
        if index < 0 or index > self.size:
            raise Exception("超出数组实际元素范围！")
        # 从右向左循环，逐个元素向左挪一位
        for i in range(self.size-1, -1, -1):
            self.array[i+1] = self.array[i]
        # 腾出的位置放新元素
        self.array[index] = element
        self.size += 1

    def insert_v2(self, index, element):
        """需要扩容的情况"""
        # 判断访问下标是否超出范围
        if index < 0 or index > self.size:
            raise Exception("超出数组实际元素范围！")
        # 如果实际元素到达数组容量上限，数组扩容
        if self.size >= len(self.array):
            self.resize()
        # 从右向左循环，逐个元素向左挪一位
        for i in range(self.size-1, -1, -1):
            self.array[i+1] = self.array[i]
        # 腾出的位置放新元素
        self.array[index] = element
        self.size += 1

    def resize(self):
        array_new = [None] * len(self.array) * 2
        # 从旧数组复制到新数组
        for i in range(self.size):
            array_new[i] = self.array[i]
        self.array = array_new

    def remove(self, index):
        if index < 0 or index >= self.size:
            raise Exception("超出数组实际元素范围！")
        # 从左向右，逐个元素向左挪一位
        for i in range(index, self.size):
            self.array[i] = self.array[i+1]
        self.size -= 1

    def output(self):
        for i in range(self.size):
            print(self.array[i])
        print(self.array)


array = MyArray(4)
array.insert_v2(0, 10)
array.insert_v2(0, 11)
array.insert_v2(0, 12)
array.insert_v2(0, 13)
array.insert_v2(0, 14)
array.insert_v2(0, 15)
array.insert_v2(1, 16)

array.remove(3)

array.output()