package main

import "fmt"

var c int = 20

func main(){
	var a, b, c int 
	a = 10
	b = 20
	fmt.Println(c)
	c = a + b
	fmt.Println("结果： a = %d, b = %d and c = %d\n", a, b, c)
}