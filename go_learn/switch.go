package main

import (
	"fmt"
)

func main(){
	a :=1
	switch {
	case a >= 0:
		fmt.Println("a = 0")
		fallthrough    // 如果匹配成功则继续执行以下匹配
	case a >= 1:
		fmt.Println("a = 1")  // 默认的匹配到结果会默认跳出case 不在执行下边的代码
	default:
		fmt.Println("None")
	}
}