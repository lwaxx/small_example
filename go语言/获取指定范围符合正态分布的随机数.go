package main

import (
	"fmt"
	"math"
	"math/rand"
	"time"
)

func GetGaussRandomNum(min, max int64) int64 {
	σ := (float64(min) + float64(max)) / 2
	μ := (float64(max) - σ) / 3
	rand.Seed(time.Now().UnixNano())
	x := rand.Float64()
	x1 := rand.Float64()
	a := math.Cos(2*math.Pi*x) * math.Sqrt((-2)*math.Log(x1))
	result := a*μ + σ
	return int64(result)
}

func main() {
	for i := 1; i < 1000; i++ {
		result := GetGaussRandomNum(30, 60)
		fmt.Println(result)
	}
}
