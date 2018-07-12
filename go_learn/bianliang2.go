package main

import "fmt"

var x, y int

var (
	a int
	b bool
)

var c, d int = 1, 3
var e, f = 123, "hello"

func main(){
	g, h := 333, "world"
	fmt.Println(&x, y, a, b, c, d, e, f, g, h)
}