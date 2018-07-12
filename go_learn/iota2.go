package main

import "fmt"

func main(){
	const (
		a = "aaa"
		b  // 这样省略则代表与上边的变量相同
		c
		d
		e
	)
	fmt.Println(a, b, c, d, e)
}