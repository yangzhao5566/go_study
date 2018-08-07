package main

import "fmt"

type field struct {
	name string
}


func (p *field) print() {
	fmt.Println(p.name)
}


func main() {
	datal := []*field{{"one"}, {"two"}, {"three"}}
	for _, v := range datal {
		defer v.print()
	}

	data2 := []field{{"four"}, {"five"}, {"six"}}
	for _, v := range data2 {
		defer v.print()
	}
}
