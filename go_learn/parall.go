package main

import "runtime"

type Vector []float64

func(v Vector) DoSome(i, n int, u Vector, c chan int) {
	for ; i < n; i++ {
		v[i] += u.Op(v[i])
	}
	c <- 1
}

counst NCPU = 16

func (v Vector) DoAll(u Vector) {
	c := make(chan int, NCPU)
	runtime.GOMAXPROCS(16)  // 设置运行时16核心
	runtime.NumCPU()
	for i := 0; i < NCPU; i++ {
		go v.DoSome(i*len(v)/ NCPU, (i+1)*len(v)/NCPU, u, c)
	}
	for i := 0; i < NCPU; i++ {
		<-c
	}
	//
}


//  设置go语言使用cpu核心的值