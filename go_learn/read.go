package main

import "os"

for _, filename := range filenames {
	f, err := os.Open(fliename)
	if err != nil {
		return err
	}
	defer f.Close()
	// 这样写有问题 会导致系统的文件描述符耗尽
}

// 一种解决办法是把里边的函数封封装成另外一个函数

for _, filename := range flienames {
	if err := doFile(filename); err != nil {
	return err
	}
}
func doFile(filename string) error {
	f, err := os.Open(filename)
	if err != nil {
		return err
	}
	defer f.Close()
}
