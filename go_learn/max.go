package main

import "fmt"

func max(num1, num2 int) int {
	var result int 
	if (num1 > num2){
		result = num1
	}else {
		result = num2
	}
	return result
}

func swap(x, y string) (string, string) {
	return x, y
}

func main(){
	fmt.Println(max(1, 3))
	fmt.Println(swap("a", "b"))
}