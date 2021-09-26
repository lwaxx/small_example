package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
	// go取随机数需要指定一个随机种子
	// 种子一般使用当前的系统时间，这是完全随机的。
	rand.Seed(time.Now().UnixNano())
	num := rand.Intn(10-5+1) + 5 //[5,10]
	fmt.Println(num)
	fmt.Println("==========分界线==========")

	// 循环100次取值
	for i := 0; i < 100; i++ {
		rand.Seed(time.Now().UnixNano())
		num := rand.Intn(10-5+1) + 5 //[5,10)
		fmt.Println(num)
	}

}
