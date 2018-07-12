package main

import "fmt"

func main(){
	var a, b = 1, 1
	for {
		a++
		if a > 3 {
			break
		}
		fmt.Println(a)
	}
	for b<=3 {
		b++
		fmt.Println(b)
	}

	for c := 0; c < 3; c++ {
		c ++
		fmt.Println(c)
	}
	fmt.Println("over")
}