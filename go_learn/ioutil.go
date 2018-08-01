package ioutil

import (
	"os"
	"github.com/derekparker/delve/pkg/proc/core"
	"io"
)

func ReadFile(filename string)([]byte, error){
	f, err := os.Open(filename)
	if err != nil {
		return nil, err
	}
	defer f.Close()
	return ReadAll(f)
}
