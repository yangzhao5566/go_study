package main

import (
	"fmt"
)

type Values map[string][]string

func main(){
	m := Values{"lang":{"en"}}
	m.Add("item", "1")
	m.Add("item", "2")
	fmt.Println(m.Get("lang"))
	fmt.Println(m.Get("q")) // ""
	fmt.Println(m.Get("item")) // "1" (first value)
	fmt.Println(m["item"]) // "[1 2]" (direct map access)
}

func (v Values) Get(key string) string {
	if vs := v[key]; len(vs) > 0 {
		return vs[0]
	}
	return ""
}

func (v Values) Add(key, value string) {
	v[key] = append(v[key], value)
}

