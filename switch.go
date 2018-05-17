package main

import "fmt"

func main() {
	switch a := 1{
		// 这样a是一个局部变量
	case a>=0 :
		fmt.Println("a=0")
		fallthrough
	case a>=1:
		fmt.Println("a=1")
	default:
		fmt.Println("None")
	}
}