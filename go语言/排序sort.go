package main

import (
	"fmt"
	"sort"
)

/*
数据的格式如下：
s=[
    {"no":21,"score":90},
    {"no":21,"score":80},
    {"no":25,"score":100},
    {"no":20,"score":66},
]
*/

func TestSortSliceMap() {
	m1 := map[string]int{"no": 21, "score": 90}
	m2 := map[string]int{"no": 21, "score": 80}
	m3 := map[string]int{"no": 25, "score": 100}
	m4 := map[string]int{"no": 20, "score": 66}

	s1 := []map[string]int{m1, m2, m3, m4}

	// 排序后
	fmt.Println("排序前s1: ", s1)

	// 先根据no排序，no一样的话再根据score排序 ———— 从小到大排序
	sort.Slice(s1, func(i, j int) bool {
		// if s1[i]["no"] == s1[j]["no"] {
		// 	return s1[i]["score"] < s1[j]["score"]
		// }
		return s1[i]["no"] > s1[j]["no"] // 从大到小排序
	})

	// 排序后
	fmt.Println("排序后s1: ", s1)

	/*
	   结果：
	   排序前s1:  [map[no:21 score:90] map[no:21 score:80] map[no:25 score:100] map[no:20 score:66]]
	   排序后s1:  [map[no:20 score:66] map[no:21 score:80] map[no:21 score:90] map[no:25 score:100]]
	*/
}

func main() {
	TestSortSliceMap()
}
