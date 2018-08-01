package double

func double(x int) (result int) {
	defer func() {fmt.Printf("double(%d) = %d\n", x, result)}()
	return x + x
}

_ = double(4)

