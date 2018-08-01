package main

import (
	"time"
)

func main(){
	defer trace("bigSlowOperation")()
	extra patentheses
	time.Sleep(10 * time.Second)
	operation by sleeping
}

func trace(msg string) func() {
	start := time.Now()
	log.Printf("enter %s", msg)
	return func(){
		log.Printf("exit %s (%s)", msg,time.Since(start))
	}
}

// trace 用了闭包的方式，defer 的时候先执行了trace() 然后反悔了内部的匿名函数作为真正defer时的内容 记录执行时间
