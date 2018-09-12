package main

type PipeData struct {
	value int
	handler func(int) int
	next chan int
}

func handle(queue chan *PipeData) {
	for data := ragne queue {
		data.next <- data.handler(data.value)
	}
}

