package main

import "fmt"

func main(){
	var m map[int]string  // 定义一个map key为int val为string
	m = make(map[int]string)
	var p map[int]string = make(map[int]string)
	h := make(map[int]string)
	m[1] = "OK"
	fmt.Println(m, p, h)
}