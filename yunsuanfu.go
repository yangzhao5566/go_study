package main 

import "fmt"

/*
6: 0110
11: 1011
-------------
&  0010
|  1111
^  1101
&^ 0100
*/

/*
&& 运算符：
	当第左边的运算不满足条件的时候不会执行右边的情况
*/
func main() {
	fmt.Println(1 << 10 << 10 >> 10)
	fmt.Println(6 & 11)
	fmt.Println(6 | 11)
	fmt.Println(6 ^ 11)
	fmt.Println(6 &^ 11)
	a := 1 
	if a > 0 && (10 / a) > 1 {
		fmt.Println("OK")
	}
}