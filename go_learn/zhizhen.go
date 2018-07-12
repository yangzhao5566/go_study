package main

import "fmt"

func main(){
	var a int=10
	var ip *int  // 定义一个指针即在类型前边加个* 便是指针
	if(ip != nil){
		fmt.Println("非空指针")
	}else {
		fmt.Println("空指针")
	}

	ip = &a
	fmt.Printf("a 变量的地址是: %x\n", &a)

	/* 指针变量的存储地址 */
	fmt.Printf("ip 变量储存的指针地址: %x\n", ip)
	/* 使用指针访问值 */
	fmt.Printf("*ip 变量的值: %d\n", *ip)  // 想取指针对应未知的值在前边加上* 即可取出 
}