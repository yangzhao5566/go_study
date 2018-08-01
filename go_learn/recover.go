package main

import "fmt"

func soleTitle(doc *html.Node) (title string, err error) {
	type bailout struct {}
	defer func() {
		switch p := recover(); p {
		case nil;
		case bailout{}:
			err = fmt.Errorf("multiple title elements")
		default:
			panic(p)
		}
	}()
}

