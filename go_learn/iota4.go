package main

import "fmt"

const (
	i = 1<<1
	j = 3 << 2
	k
	l
)

func main(){
	fmt.Println("i=",i)
    fmt.Println("j=",j)
    fmt.Println("k=",k)
    fmt.Println("l=",l)
}