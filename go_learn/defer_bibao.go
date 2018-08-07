package main

import "fmt"

func main()  {
	var i int = 1

	defer func() {
		fmt.Println("result =>", func() int{return i * 2})
	}()
	i++
}
