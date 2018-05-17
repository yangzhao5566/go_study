package main

import (
	"fmt"
)

// 在常量表达式中只能出现常量和内置函数
const a int = 1
const b = "A"

const (
	c = "123"
	d = len(c)
	e = a + 2
	f
)
//  常量的枚举
// 每遇到一个iota就会从零开始计算
// 常量一遍都写成大写
const (
	g = "A"
	h 
	i = iota
	j
)

func main() {
	fmt.Println(c, d, e, f, g, h, i, j)
}

