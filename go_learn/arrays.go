package main 

import "fmt"

var a [3]int

func main(){
	fmt.Println(a[0])
	fmt.Println(a[len(a)-1])
	for _, v := range a {
		fmt.Println(v)
	}
}