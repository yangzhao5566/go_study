package main

import (
	"net/http"
	"io"
	"log"
	"os"
	"io/ioutil"
	"html/template"
)

const (
	UPLOAD_DIR = "./uploads"
)

//func uploadHandler(w http.ResponseWriter, r *http.Request) {
//	if r.Method == "GET" {
//		io.WriteString(w,  "<form method=\"POST\" action=\"/upload\" "+
//			" enctype=\"multipart/form-data\">"+
//			"Choose an image to upload: <input name=\"image\" type=\"file\" />"+
//			"<input type=\"submit\" value=\"Upload\" />"+
//			"</form>")
//		return
//	}
//}

func uploadHandler(w http.ResponseWriter, r *http.Request) {
	if r.Method == "GET" {
		if err := renderHtml(w, "upload", nil); err != nil {
			http.Error(w, err.Error(),
				http.StatusInternalServerError)
			return
		}
		//io.WriteString(w,  "<form method=\"POST\" action=\"/upload\" "+
		//	" enctype=\"multipart/form-data\">"+
		//	"Choose an image to upload: <input name=\"image\" type=\"file\" />"+
		//	"<input type=\"submit\" value=\"Upload\" />"+
		//	"</form>")
		//return
	}
	if r.Method == "POST" {
		f, h, err := r.FormFile("image")
		t, err := template.ParseFiles("upload.html")
		if err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
			return
		}
		t.Execute(w, nil)
		filename := h.Filename
		defer f.Close()
		t, err := os.Create(UPLOAD_DIR + "/" + filename)
		if err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
			return
		}
		defer t.Close()
		if _, err := io.Copy(t, f); err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
			return
		}
		http.Redirect(w, r, "/view?id="+filename, http.StatusFound)
	}
}

func isExists(path string) bool {
	_, err := os.Stat(path)
	if err == nil {
		return true
	}
	return os.IsExist(err)
}

func viewHandler(w http.ResponseWriter, r *http.Request) {
	imageId := r.FormValue("id")
	imagePath := UPLOAD_DIR + "/" + imageId
	//err := isExists(imagePath)
	w.Header().Set("Content-Type", "image")
	http.ServeFile(w, r, imagePath)
}

func renderHtml(w http.ResponseWriter, tmpl string, locals map[string]interface{}) err error {
	t, err = template.ParseFiles(tmpl + ".html")
	if err != nil {
		return
	}
	err = t.Execute(w, locals)
}


func listHandler(w http.ResponseWriter, r *http.Request) {
	fileInfoArr, err := ioutil.ReadDir("./uploads")
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	//locals := make(map[string]interface{})
	//images := []string{}
	var listHtml string
	for _, fileInfo := range fileInfoArr {
		imgid := fileInfo.Name
		listHtml += "<li><a href=\"/view?id="+imgid+"\">imgid</a></li>"
		io.WriteString(w, "<ol>"+listHtml+"</ol>")
	}
}

func main() {
	http.HandleFunc("/upload", uploadHandler)
	http.HandleFunc("/upload", viewHandler)
	http.HandleFunc("/", listHandler)
	err := http.ListenAndServe(":8090",nil)
	if err != nil {
		log.Fatal("ListenAndServe:", err.Error())
	}
}