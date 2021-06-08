package main

import (
	"fmt"
	"time"
)

func main() {
	current := time.Now().Unix()

	fmt.Println(current)

	BeforeDate := "2019-09-01 15:48:00"
	loc, _ := time.LoadLocation("Local") //获取时区
	tmp, _ := time.ParseInLocation("2006-01-02 15:04:05", BeforeDate, loc)
	timestamp := tmp.Unix() //转化为时间戳 类型是int64

	res := (current - timestamp) / 86400 //相差值
	fmt.Println(res)
}
