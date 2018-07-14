package main

import "fmt"

func main(){
	countryCapitalMap := map[string]string{"France": "Paris", "Italy": "Rome", "Japan": "Tokyo", "India": "New delhi"}
	fmt.Println("原始地图")
	for k,v := range countryCapitalMap {
		fmt.Println(k, "首都是：", v)
		delete(countryCapitalMap, k)
	}
}