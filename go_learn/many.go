package main

import "fmt"

func myfunc(args ...int) {
	for _, arg := range args {
		fmt.Println(arg)
	}
}
