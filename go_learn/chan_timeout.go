package main

import "time"

func main() {
	timeout := make(chan bool, 1)
	go func() {
		time.Sleep(1e9)
		timeout <- true
	}()

	select {
	case <- ch:
		// 从ch中读取到数据
	case <- timeout:
			// 一直没有从ch中读取数据，但从timeout中读取到了数据
	}
}
