package main 

import "fmt"

const (
	_ = iota
	kb float64 = 1 <<(iota * 10)
	MB
	GB
	TB
	PB
	EB
	ZB
	YB
)

func main(){
	fmt.Println(kb, MB, GB, TB)
}