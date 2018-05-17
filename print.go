package main

// 包起别名 import std "fmt"
import std "fmt"
// import . "fmt"  省略调用  相当于 from collection import * 


// 常量的定义
const PI = 3.14

// 常量定义组
const (
	const1 = "1"
	const2 = 2
)

// 全局变量的声明与赋值
var name = "gopher"

// 全局变量的声明，在函数体内不能这么用
var (
	name1 = "1"
	name2 = 2
)

// 一般类型声明
var newType int
var (
	type1 float32
	type2 string
	type3 byte
)

// 结构的声明
type gopher struct{}

// 接口声明
type golang interface{}


func main() {
	std.Printf("hello world! 你好，世界！")
}

// 可见性规则： go语言中使用大小写来决定常量变量类型接口结构或者函数能否可以被
// 包外部所调用 -- 规则: 函数名首字母小写即为private  函数名首字母大写即为public即可以为外部调用
