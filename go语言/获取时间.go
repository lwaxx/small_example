package main

import (
	"fmt"
	"time"
)

const (
	DATE_LAYOUT        = "20060102"
	DateHourLayout     = "2006010215"
	DateHourHalfLayout = "200601021504"
)

func getCurHourStr() string {
	now := time.Now()
	issue_no := now.Format(DateHourLayout)
	return issue_no
}

func getCurHalfHourStr() string {
	now := time.Now()
	y, m, d := now.Date()
	h, mi, _ := now.Clock()
	if mi < 30 {
		mi = 0
	} else {
		mi = 30
	}
	tm := time.Date(y, m, d, h, mi, 0, 0, time.Local)
	dateHourStr := tm.Format(DateHourHalfLayout)
	return dateHourStr
}

func main() {
	// 2022042615
	issue_no_hour := getCurHourStr()
	fmt.Println(issue_no_hour)

	// 202204251530
	issue_no_half_hour := getCurHalfHourStr()
	fmt.Println(issue_no_half_hour)
}
