package main

import "fmt"

func main(){
	var countryCapitalMap map[string]string  //创建集合
	countryCapitalMap = make(map[string]string)

	new_country := make(map[string]string)

	// map插入key -value 
	countryCapitalMap["France"] = "Paris"
	countryCapitalMap [ "Italy" ] = "罗马"
    countryCapitalMap [ "Japan" ] = "东京"
	countryCapitalMap [ "India " ] = "新德里"
	
	for country := range countryCapitalMap {
		fmt.Println(country, "首都是", countryCapitalMap[country])
	}

	for k, v := range countryCapitalMap {
		new_country[k] = v
		fmt.Println(k, v)
	}

	fmt.Println(new_country)
}