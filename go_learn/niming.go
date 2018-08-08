package main

func main() {
	f := func(x, y int) int {
		return x + y
	}

	func(ch chan int) {
		ch <- ACK
	} (reply_chan)
}
