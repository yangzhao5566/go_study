package main

import "fmt"

type Celsius float64

func (c Celsius) String() string {
	return fmt.Sprintf("Celsius is %g ", c)
}

func main(){
	c := Celsius(212.0)
	fmt.Printf("%s \n", c.String())
}