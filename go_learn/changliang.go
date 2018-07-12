package main

import "fmt"

func main(){
	const LENGTH int = 10
	const WIDTH int = 5
	var area int 
	const a, b, c = 1, false, "str" // 多变量赋值
	area = LENGTH * WIDTH
	fmt.Printf("面积为：%d \n", area)
	fmt.Println()
	fmt.Println(a,b,c)
}