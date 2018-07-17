package main

import "fmt"

func main() {
	q := [...]int {12, 22, 343}
	p := [4]int {1,2,3,4}
	fmt.Printf("%T\n", q)
	fmt.Printf("%T\n", p)
}