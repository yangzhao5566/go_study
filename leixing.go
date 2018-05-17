package main

import (
	"fmt"
	"math"
	"strconv"
)

// 类型别名
type (
	byte int8
	rune int32
	文本 string
)

func main() {
	var f 文本
	var a int32
	var b string
	var c []int 
	var d [1] bool
	var g int = 1
	var aa float32 = 65.1
	h6 := int(aa)
	h := 1
	f = "中文类型名"
	var h1, h2, h3 int = 1, 2, 3
	h4, _ := 4, 5
	fmt.Println(b)
	fmt.Println(a)
	fmt.Println(c)
	fmt.Println(d)
	fmt.Println(math.MaxInt32)
	fmt.Println(f)
	fmt.Println(g)
	fmt.Println(h)
	fmt.Println(h1, h2, h3)
	fmt.Println(h4)
	fmt.Println(h6)
	fmt.Println(string(h6))
	fmt.Println(strconv.Atoi("65"))
	fmt.Println(strconv.Itoa(h6))
}