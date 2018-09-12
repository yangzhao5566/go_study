package main

import "sync"

var a string
var once sync.Once

func setup() {
	a = "hello, world"
}

func doprint() {
	once.Do(setup)
	print(a)
}

func twoprint() {
	go doprint()
	go doprint()
}


// once的Do()方法可以保证在全局范围内只调用指定的函数一次（这里指
//setup()函数）

// 而且所有其他goroutine在调用到此语句时，将会先被阻塞，直至全局唯一的
//once.Do()调用结束后才继续。

// 自己实现如下

var done bool = false

func setup() {
	a = "hello, world"
	done = true
}

func doprint() {
	if !done {
		setup()
	}
	print(a)
}

