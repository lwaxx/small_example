package main

import "strconv"

// go语言string、int、int64互相转换

func main() {
	//string到int
	int, err := strconv.Atoi(string)

	//string到int64
	int64, err := strconv.ParseInt(string, 10, 64)

	//int到string
	string := strconv.Itoa(int)

	//int64到string
	string := strconv.FormatInt(int64, 10)

	//string到float32(float64)
	float, err := strconv.ParseFloat(string, 32/64)

	//float到string
	string := strconv.FormatFloat(float32, 'E', -1, 32)
	string := strconv.FormatFloat(float64, 'E', -1, 64)
	// 'b' (-ddddp±ddd，二进制指数)
	// 'e' (-d.dddde±dd，十进制指数)
	// 'E' (-d.ddddE±dd，十进制指数)
	// 'f' (-ddd.dddd，没有指数)
	// 'g' ('e':大指数，'f':其它情况)
	// 'G' ('E':大指数，'f':其它情况)

}
