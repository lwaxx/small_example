package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"os"
)

type anInfo struct {
	Uid     string `json:"uid"`
	BizType int    `json:"biz_type"`
	BoxNum  int    `json:"box_num"`
}

type rrr struct {
	Iterms []*anInfo `json:"data"`
}

func main() {
	f, err := os.Open("pp.json")
	if err != nil {
		return
	}
	confJson, err := ioutil.ReadAll(f)
	f.Close()
	// fmt.Println(confJson)

	var res rrr
	err = json.Unmarshal(confJson, &res)
	item_list := res.Iterms
	fmt.Printf("%T", item_list)
	for i, _ := range item_list {
		// if item_list[i] != nil {

		// }
		fmt.Printf("uid: %s\n", item_list[i].Uid)
		fmt.Printf("biz_type: %d\n", item_list[i].BizType)
		fmt.Printf("box_num: %d\n", item_list[i].BoxNum)

	}
}
