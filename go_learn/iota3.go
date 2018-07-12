package main

import "fmt"

const (
	i = 1 << iota
	j = 3 << iota
	k
	l
)

/* 输出结果
i= 1
j= 6
k= 12
l= 24
*/

func main(){
	fmt.Println("i=",i)
    fmt.Println("j=",j)
    fmt.Println("k=",k)
    fmt.Println("l=",l)
}