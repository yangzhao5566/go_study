package main
import "fmt"

var name1, name2, name3 = "张三", "李四", "x"
/* 用于声明多个变量*/
var (
	s3 string   //这种饮食分解关键字的写法一般用于声明全局变量
	s4 int8
	s5 = 33
	s6 = "44"
)  

func main(){
	var vname1, vname2, vname3 string  // 只能用来声明局部变量
	s1, s2 := "张三", "李四"   //只能在函数中使用声明变量 并且声明的变量
	vname1 = "aaa"
	vname2 = "bbb"
	vname3 = "ccc"
	fmt.Println(vname1, vname2, vname3, name1, name2, name3, s1, s2)
	fmt.Println(s3, s4, s5, s6)
}
