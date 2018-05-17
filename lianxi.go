package main

import "fmt"

const (
	B float64 = 1 << (iota * 10)
	KB 
	MB
	GB
	TB
)

func main() {
	a := 1
	a++  // -- ++ 不能放到运算的右边，只能像这样写
	if a:=1; a>1 {
		fmt.Println("ok")
		//当我不有同名a的时候 在if条件中定义a则在if语句内部会使用内部的
	}
	var p *int = &a
	fmt.Println(p)
	fmt.Println(*p)
	fmt.Println(TB)
}