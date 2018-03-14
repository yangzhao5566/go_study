package main

import "fmt"

func main() {
	nums :=[]int{2, 3, 4}
	sum := 0
	for _, num := range nums {
		sum += num
	}
	fmt.Println("sum:", sum)
	// range 用来便利数组和切片的时候返回索引和元素值
	// 如果我们不要关心索引可以使用一个下划线(_)来忽略这个返回值
	for i, num := range nums {
		if num == 3 {
			fmt.Println("index:", i)
		}
	}
	kvs := map[string]string{"a": "apple", "b": "banana"}
	for k, v := range kvs {
		fmt.Println("%s -> %s\n", k, v)
	}

	// range函数用来遍历字符串时，返回Unicode代码点。
    // 第一个返回值是每个字符的起始字节的索引，第二个是字符代码点，
	// 因为Go的字符串是由字节组成的，多个字节组成一个rune类型字符。
	//  若想不显示字符代码 可以将%s 改成%c
    for i, c := range "go" {
        fmt.Println(i, c)
    }

	// 总结： go语言中的range 有点类似python中的enumerate 
	// 当range列表或者字符串时返回索引和对应字段，range字典事返回k,v  
	//  文章来源https://studygolang.com/articles/1952
}
