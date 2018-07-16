package main

import "fmt"

func main(){
	p := new(int)  // 创建一个匿名变量，返回对应变量的地址
	fmt.Println(p)
	*p = 2 
	fmt.Println(*p)
}