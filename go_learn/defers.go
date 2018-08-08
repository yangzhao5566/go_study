package main

import (
	"os"
	"io"
)

func CopyFile(dst, src string) {
	srcFile, err := os.Open(src)
	if err != nil {
		return
	}

	defer srcFile.Close()
	dstFile, err := os.Create(dstName)
	if err != nil {
		return
	}

	defer dstFile.Close()
	return io.Copy(dstFile, srcFile)
}
