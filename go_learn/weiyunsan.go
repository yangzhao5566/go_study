package main

import "fmt"

func main(){
	var a uint = 16
	var b uint = 13
	var c uint = 0
	c = a & b
	fmt.Printf("%d\n",c)

	c = a | b
	fmt.Printf("%d\n",c)

	c = a ^ b
	fmt.Printf("%d\n",c)
	c = a << 2
	fmt.Printf("%d\n",c)

	c = a >> 2
	fmt.Printf("%d\n",c)
}