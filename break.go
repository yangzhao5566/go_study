package main

import "fmt"

// goto break  continue
func main() {
	LABEL1:
		for i:=0; i<10; i++ {
			// if i > 3{
			// 	break LABEL1
			// }
			for {
				fmt.Println(i)
				goto LABEL1
			}
		}
	fmt.Println("OK")
}