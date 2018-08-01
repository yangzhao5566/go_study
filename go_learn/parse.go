package main

import "fmt"

func Parse(input string)(s *Syntax, err error){
	defer func() {
		if p := recover(); p != nil {
			err = fmt.Errorf("internal error: %v", p)
		}
	}()
	// ...parser...
}
