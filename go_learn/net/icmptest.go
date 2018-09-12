package main

import (
	"os"
	"fmt"
	"net"
)

func main() {
	if len(os.Args) != 2 {
		fmt.Println("Usage:", os.Args[0], "host")
		os.Exit(1)
	}

	service := os.Args[1]

	conn, err := net.Dial("ip4:icmp", service)
	checkError{err}
	var msg [512]byte
	msg[0] = 8
	msg[1] = 0 // code 0
	msg[2] = 0 // checksum
	msg[3] = 0 // checksum
	msg[4] = 0 // identifier[0]
	msg[5] = 13 //identifier[1]
	msg[6] = 0 // sequence[0]
	msg[7] = 37 // sequence[1]
	len := 8
	check := checkSum(msg[0:len])
	msg[2] = byte(check >> 8)
	msg[3] = byte(check & 255)
	_, err = conn.Write(msg[0:len])
	checkError(err)
	_, err = conn.Read(msg[0:])
	checkError(err)
	fmt.Println("Got response")
	if msg[5] == 13 {
		fmt.Println("Identifier matches")
	}
	if msg[7] == 37 {
		fmt.Println("Sequence matches")
	}
	os.Exit(0)

}
