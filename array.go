package main

import "fmt"

func main() {
	var a [2]int  // a为只能存放两个int类型的数组
	var b [1]int  // a != b 因为b和a的存放变量的个数不同
	var c [2]string
	d := [...]int{1, 2, 3, 4, 5}  // 通过三个点让编译器自己计算赋值里边是几个值
	e := [...]int{1:1, 2:2, 3:3, 5:4, 4:5}
	f := [2]string{"a", "b"}
	// 指针 运算符就是简单的&和* &取地址，*解析地址
	var p *[100]int = &e
	fmt.Println(a, b, c, d, f, e)  // a 默认值为[0,0]
	fmt.Println(p)
}