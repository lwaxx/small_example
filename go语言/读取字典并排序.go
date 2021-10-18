package main

import (
	"fmt"
	"math/rand"
	"sort"
	"time"
)

var (
	onevoneAnchorList = map[int64]map[string]int64{
		326882506324376282: {"l": 240000, "h": 300000},
		373059394499291777: {"l": 180000, "h": 220000},
		364376599611317069: {"l": 120000, "h": 150000},
		340468497490453090: {"l": 120000, "h": 150000},
		385564412850809375: {"l": 80000, "h": 120000},
		302406787223557864: {"l": 80000, "h": 100000},
		226207139075479200: {"l": 50000, "h": 80000},
	}
)

type CharmRankResult struct {
	AnchorId    int64 `json:"b"`
	Platform_id int64 `json:"p"`
	IncomeCoin  int64 `json:"c"`
	// Source      int64  `json:"s"`
	// Avatar      string `json:"a"`
	// Name        string `json:"n"`
	Rank int64 `json:"r"`
	// UpRank      int64  `json:"u"`
	// JumpStatus  int    `json:"nj"` // 是否可跳个人页, 0-可跳, 1-不可跳
	// Mysteryer   int    `json:"ms"` // 神秘人开关, 0-未开启神秘人, 1-开启神秘人
	// Live        int64  `json:"le"` // 开播状态
	// Template    string `json:"t"`
}

func Read() {
	cr := []*CharmRankResult{}
	cr = append(cr, &CharmRankResult{
		AnchorId:   226207139075479200,
		IncomeCoin: 100,
	})
	fmt.Println(*cr[0])
	fmt.Println("=========")
	for k, v := range onevoneAnchorList {
		// 取随机值
		rand.Seed(time.Now().UnixNano())
		num := rand.Int63n(v["h"]-v["l"]) + v["l"]
		// fmt.Println(k, num)

		for i, j := range cr {
			if (*j).AnchorId == k {
				// (*j).IncomeCoin = num
				cr = append(cr[:i], cr[i+1:]...)
			}
		}

		cr = append(cr, &CharmRankResult{
			AnchorId:   k,
			IncomeCoin: num,
		})

	}
	// fmt.Println("排序前: ", *cr[0], *cr[1], *cr[2], *cr[3], *cr[4], *cr[5], *cr[6])
	sort.Slice(cr, func(i, j int) bool {
		return (*cr[i]).IncomeCoin < (*cr[j]).IncomeCoin
	})
	// fmt.Println("排序后: ", *cr[0], *cr[1], *cr[2], *cr[3], *cr[4], *cr[5], *cr[6])

	for k, v := range cr {
		(*v).Rank = int64(k + 1)

	}
	// fmt.Println("排序后: ", *cr[0], *cr[1], *cr[2], *cr[3], *cr[4], *cr[5], *cr[6])

	fmt.Println(cr)
	fmt.Println(cr[:6])
}

func main() {
	Read()
}
