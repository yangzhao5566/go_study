package main

import "fmt"

func main() {
	str := "hello, 世界"

	//n := len(str)
	//for i := 0; i < n; i++ {
	//	ch := str[i]
	//	fmt.Println(i, ch)
	//}

	for i, ch := range str {
		fmt.Println(i, ch)
	}
}
