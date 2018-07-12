package main

import (
	"unsafe"
	"fmt"
)

const (
	a = "abc"
	b = len(a)
	c = unsafe.Sizeof(a)
)

func main(){
	fmt.Println(a, b, c)
}