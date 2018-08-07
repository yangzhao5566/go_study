package main

import "fmt"

type field struct {
	name string
}

func print(p *field) {
	fmt.Println(p.name)
}

func main() {
	data1 := []*field{{"one"}, {"two"}, {"three"}}
	for _, v := range data1 {
		defer print(v)
	}

	data2 := []field{{"four"}, {"five"}, {"six"}}

	for _, v := range data2 {
		defer print(&v)
	}
}