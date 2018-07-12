package main

import "fmt"

func swap(x *int, y *int){
	*x, *y = *y, *x
}

func main(){
	var a int = 10
	var b int = 20
	swap(&a, &b)
	fmt.Printf("交换后 a 的值 : %d\n", a )
	fmt.Printf("交换后 b 的值 : %d\n", b )
}