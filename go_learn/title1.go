package main

import (
	"net/http"
	"strings"
	"fmt"
)

func title(url string) error {
	resp, err = http.Get(url)
	if err != nil {
		return err
	}
	defer resp.Body.Close()
	ct := resp.Header.Get("Content-Type")
	if ct != "text/html" && !strings.HasPrefix(ct,"text/html;"){
		//resp.Body.Close()
		return fmt.Errorf("%s has type %s, not text/html",url, ct)
	}
	if err != nil {
		return fmt.Errorf("parsing %s as HTML: %v", url,err)
	}
	visitNode := func(n *html.Node){
		if n.Type == html.ElementNode && n.Data == "title"&&n.FirstChild != nil {
			fmt.Println(n.FirstChild.Data)
		}
	}
	forEachNode(doc, visitNode, nil)
	return nil
}

