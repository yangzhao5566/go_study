package main

import "fmt"

func main(){
	var p *int 
	var b int = 3
	var x, y int
	fmt.Println(p)   //  任何类型未使用的指针的零值都是nil
	fmt.Println(&x, &y)
	fmt.Println(b)
}