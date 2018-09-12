package main

import (
	"fmt"
	"io"
	"os"
	"net/http"
)

func main() {
	resp, err := http.Get("http://www.baidu.com")
	if err != nil {
		fmt.Println(err)
		return
	}
	//defer resp.Body.close()
	io.Copy(os.Stdout, resp.Body)
}
