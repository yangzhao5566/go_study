package main

import "fmt"


func main() {
	s1 := make([]int, 3, 6)
	s2 := s1[2:4]
	fmt.Println(cap(s2))
	fmt.Println("%p", s1)
	s1 = append(s1, 1, 2, 3)
	fmt.Printf("%v %p\n", s1, s1)
	s1 = append(s1, 1, 2, 3)
	fmt.Println("%v %p", s1, s1)
}