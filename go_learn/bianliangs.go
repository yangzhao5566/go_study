package main

func main()  {
	var v1 int
	var v2 string
	var v2 [10]int
	var v4  []int
	var v5 struct {
		f int
	}
	var v6 *int
	var v7 map[string]int
	var v8 func(a int) int

	var (
		v1 int
		v2 string
	)

	var v1 int = 10
	var v2 = 10
	v3 := 10

	const Pi float64 = 3.1415926
	const zero = 0.0
	const (
		size int64 = 1024
		eof = -1
	)

	const u, v float32 = 0, 3
	const a, b, c = 3, 4, "foo"

	var v1 bool = true
	v2 := (1 == 2)


}
