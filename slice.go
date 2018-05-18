package main

import "fmt"

func main() {
	a := [10]int{}
	s1 := a[5:10]
	s2 := make([]int, 3, 10)  // 先分10个当不够的时候会成倍增加
	fmt.Println(s2, cap(s2))
	fmt.Println(s1)
}