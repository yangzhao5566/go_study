package main

import "fmt"

func main(){
	var a bool = true
	var b bool = false
	if (a && b){
		fmt.Printf("true")
	}
	if (a||b){
		fmt.Printf("bbb")
	}
	a = false
	b = true
	if (a && b){
		fmt.Printf("ccc")
	}else{
		fmt.Printf("ddd")
	}
}