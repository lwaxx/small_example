package main

/*
	go 测试概率，10000分
	eg. 41% --> 4100
*/

import (
	"fmt"
	"math/rand"
	"time"
)

func Sum_int_list(li []int) int {
	var s int
	for _, n := range li {
		s += n
	}
	return s
}

// 概率数组 随机
func GetRandIdxInRateList(rate_list []int) int {
	rateLen := len(rate_list)
	if rateLen == 0 {
		return -1
	} else if rateLen == 1 {
		if rate_list[0] <= 0 {
			return -1
		}
		return 0
	}
	r := rand.New(rand.NewSource(time.Now().UnixNano()))
	t_r := Sum_int_list(rate_list)
	d := r.Intn(t_r)
	var sel_i, acc_r int
	sel_i = -1
	for i := 0; i < rateLen; i++ {
		acc_r += rate_list[i]
		if d < acc_r {
			sel_i = i
			break
		}
	}
	return sel_i
}

var (
	moon_conf = map[int64]int64{
		1: 1000,
		2: 4100,
		3: 3500,
		4: 700,
		5: 500,
		6: 200,
	}
	moon_conf1 = []int{1000, 4100, 3500, 700, 500, 200}
	a          = 0
	b          = 0
	c          = 0
	d          = 0
	e          = 0
	f          = 0
)

// func main() {
// 	for i := 0; i < 10000; i++ {
// 		sel_i := GetRandIdxInRateList(moon_conf1)
// 		if sel_i >= 0 && sel_i < len(moon_conf1) {
// 			for k, v := range moon_conf {
// 				if int(v) == moon_conf1[sel_i+1] {
// 					fmt.Println(k, moon_conf1[sel_i+1])
// 				}
// 			}
// 			ll := sel_i + 1
// 			if ll == 1 {
// 				a += 1
// 			} else if ll == 2 {
// 				b += 1
// 			} else if ll == 3 {
// 				c += 1
// 			} else if ll == 4 {
// 				d += 1
// 			} else if ll == 5 {
// 				e += 1
// 			} else {
// 				f += 1
// 			}
// 		}

// 	}

// 	fmt.Println(a)
// 	fmt.Println(b)
// 	fmt.Println(c)
// 	fmt.Println(d)
// 	fmt.Println(e)
// 	fmt.Println(f)

// 	// for k, v := range moon_conf {
// 	// 	fmt.Println(k, v)
// 	// }
// }

func GetMoonId() int64 {
	var moonId int64
	sel_i := GetRandIdxInRateList(moon_conf1)
	for k, v := range moon_conf {
		// fmt.Println(k)
		if int(v) == moon_conf1[sel_i] {
			moonId = k
		}
	}
	return moonId
}

func main() {

	for i := 0; i < 1000; i++ {
		a := GetMoonId()
		fmt.Println(a)
	}

}
