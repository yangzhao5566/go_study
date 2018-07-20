package main

import "fmt"

func equal(x, y []string) bool {
	if len(x) != len(y) {
		return false
	}
	for i := range x {
		fmt.Println(x)
		if x[i] != y[i]{
			return false
		}
	}
	return true
}