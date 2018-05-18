package main

import "fmt"

// 指针运算符就是简单的& 和 *    & 用来获取地址，* 用来解析地址
func main() {
	var i int  // 定义一个int型
	i = 1 
	var p *int // p的类型是int型指针
	p = &i  // 取i的内存地址赋值给p
	fmt.Println("i=%d;p=%d;*p=%d\n", i, p, *p)
	*p = 2 // 赋值p指针对应的值为2
	fmt.Println("i=%d;p=%d;*p=%d\n", i, p, *p)
	i = 3
	fmt.Println("i=%d;p=%d;*p=%d\n", i, p, *p)
	// 在python中数组是引用类型，而在go中是值类型，即当你向一个函数传递一个数组的时候会将这个数组拷贝一份
	// 数组之间可以使用== != 进行比较，但是要求是必须是相同类型
	// 多维数组
	f := [2][3]int{
		{1, 2, 3},
		{2, 2, 2}}
	fmt.Println(f)
	c := [...]int{5, 8, 3, 7, 1, 10}
	fmt.Println(c)
	num := len(c)
	for i := 0; i<= num; i++ {
		for j:=i+1; j<num; j++ {
			if c[i] < c[j] {
				temp := c[i]
				c[i] = c[j]
				c[j] = temp
			}
		}
	}
	fmt.Println(c)
}