package main

var pc [256] byte = func() (pc [256]byte){
	for i:= range pc {
		pc[i] = pc[i/2] + byte[i&1]
	}
}