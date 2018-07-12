package main

import "fmt"

func getAverage(arr []int, size int) int{
	var i, sum int
	var avg int 
	for i = 0; i < size; i++ {
		sum += arr[i]
	}
	avg = sum/size
	return avg
}

func main(){
	var balance = []int {10, 20, 20, 33, 44, 77, 99}
	var avg int
	avg = getAverage(balance, 3)
	fmt.Println(avg)
	fmt.Println(&avg)
}