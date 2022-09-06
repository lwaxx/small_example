package main

import "fmt"

type Books struct {
	id   int    `json:"id"`
	name string `json:"name"`
}

func main() {
	var arr = [4]int{1, 2, 3, 4}

	// 1.数组传参
	arrayArgs(arr)

	// 2.数组指针传参
	arrayPointerArgs(&arr)

	// 3.指针数组传参
	// pointerArrayArgs([4]*arr)

	// 4.结构体传参, 直接传结构体不会改变原来的值
	book := Books{1, "java"}
	fmt.Printf("yuanshi: %v\n", book)
	showBooks(book)
	fmt.Printf("yuanshi: %v\n", book)
	fmt.Println("-------------------")

	// 5.结构体指针传参，会修改原结构体的值
	fmt.Printf("yuanshi: %v\n", book)
	showBooksPointer(&book)
	fmt.Printf("yuanshi: %v\n", book)

}

// ---------- 数组相关 start -------------
func arrayArgs(arr [4]int) {
	fmt.Println(arr)
}

func arrayPointerArgs(arr *[4]int) int {
	s := 0
	for i := 0; i < len(arr); i++ {
		s += arr[i]
	}
	return s
}

func pointerArrayArgs(arr [4]*int) int {
	s := 0
	for i := 0; i < len(arr); i++ {
		s += *arr[i]
	}
	return s
}

type BoxRwdData struct {
	Ok      bool   `json:"ok,omitempty"`
	BoxId   int    `json:"b,omitempty"`
	Type    int    `json:"p,omitempty"`
	Num     int    `json:"n,omitempty"`
	RwdText string `json:"e,omitempty"`
}

func Get_Aggregation_RwdDataMap_BoxRwdData_Arr(arr []*BoxRwdData) map[int]int {
	if arr == nil {
		return nil
	}
	len1 := len(arr)
	if len1 == 0 {
		return nil
	}
	m := make(map[int]int, 0)
	for _, v := range arr {
		if v == nil {
			continue
		}
		rwd_type := v.Type
		rwd_num := v.Num
		m[rwd_type] += rwd_num
	}
	return m
}


// ---------- 数组相关 end -------------

// ---------- 结构体相关 start -------------
func showBooks(book Books) {
	book.id = 1
	book.name = "python"
	fmt.Printf("now: %v\n", book)
}

func showBooksPointer(book *Books) {
	book.id = 1
	book.name = "python"
	fmt.Printf("now: %v\n", *book)
}


type EggBox struct {
	Percent int   `json:"p"` // 占百分比
	Coin    int64 `json:"c"` // 给送礼者返钻
	GiftNum int64 `json:"n"` // 礼物个数
	GiftID  int64 `json:"i"` // 礼物id
}

type eggConfigLIst struct {
	Items []*EggBox
	sync.RWMutex
}

var eggs = eggConfigLIst{Items: make([]*EggBox, 0)}

eggs.Lock()
eggs.Items = make([]*EggBox, 0)
for _, e := range res.EggItems {
	eggs.Items = append(eggs.Items, e)
}
eggs.Unlock()


// ---------- 结构体相关 end -------------
