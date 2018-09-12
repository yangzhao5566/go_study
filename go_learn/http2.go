package main

import (
	"net/http"
	"crypto/tls"
	"crypto/rand"
	"time"
)

const SERVER_PORT = 8080
const SERVER_DOMAIN = "localhost"
const RESPONSE_TEMPLATE = "hello"

func rootHandler(w http.ResponseWriter, req *http.Request) {
	w.Header().Set("Content-Type", "text/html")
	w.Header().Set("Content-Length", fmt.Sprint(len(RESPONSE_TEMPLATE)))
	w.Write([]byte(RESPONSE_TEMPLATE))
}

func YourListenAndServeTLS(addr string, certFile string, keyFile string, handler http.Handler) error{
	config := &tls.Config{
		Rand: rand.Reader,
		Time: time.Now,
		NextProtos:[]string{"http/1.1"},
	}
	var err error
	config.Certificates = make([]tls.Certificate, 1)
}
