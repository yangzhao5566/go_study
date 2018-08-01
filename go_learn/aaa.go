package main

import (
	"fmt"
)

func main() {
	array := make(map[int]func()int)
	array[func()int{return 10}()] = func()int{return 12}
	fmt.Println(array)
}