package main

import "fmt"

func main(){
	var a int 
	var ptr *int 
	var pptr **int 
	a = 3000
	ptr = &a 
	pptr = &ptr
	fmt.Printf("变量 a = %d\n", a )
	fmt.Printf("指针变量 ptr= %d *ptr = %d\n", ptr, *ptr )
	fmt.Printf("指向指针的指针变量 pptr= %d **pptr = %d\n", pptr, **pptr)
}