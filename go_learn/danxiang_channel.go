package main

var ch1 chan int			// ch1 是一个正常的channel， 不是单向的
var ch2 chan <- float64		// ch2 是单向channel， 只用于写float64数据
var ch3 <- chan int          // 单向channel，只用于读取int数据

// channel 是一个原生类型，不仅支持被传递，还支持类型转换，
// 例如
ch4 := make(chan int)
ch5 := <- chan int(ch4)    // ch5就是一个单向的读取channel
ch6 := chan <- int(ch4)    // ch6 是一个单向的写入channel

// 单向channel用法

func Parse(ch <- chan int) {
	for value := range ch {
		fmt.Println("Parsing value", value)
	}
}


// 关闭channel
close(ch)

// 如何判断channel 是否已被关闭

x, ok := <-ch