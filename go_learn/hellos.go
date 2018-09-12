package main

import (
	"net/http"
	"io"
	"log"
	"fmt"
)

func helloHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Println(r)
	io.WriteString(w, "Hello, world")
}

func main() {
	http.HandleFunc("/hello", helloHandler)
	err := http.ListenAndServe(":8090", nil)
	if err != nil {
		log.Fatal("ListenAndServe:", err.Error())
	}
}
