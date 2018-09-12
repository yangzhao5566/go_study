package cache

import (
	"html/template"
	"io/ioutil"
	"path"
	"log"
)

const (
	TEMPLATE_DIR = "./views"
)


func init() {
	templates := make(map[string]*template.Template)
	fileInfoArr, err := ioutil.ReadDir(TEMPLATE_DIR)
	if err != nil {
		panic(err)
		return
	}
	var templateName, templatePath string
	for _, fileInfo := range fileInfoArr {
		templateName = fileInfo.Name
		if ext := path.Ext(templateName); ext != ".html" {
			continue
		}
		templatePath = TEMPLATE_DIR + "/" + templateName
		log.Println("Loading template:", templatePath)
		t := template.Must(template.ParseFiles(templatePath))
		templates[templateName] = t
	}
	//for _, tmpl := range []string{"upload", "list"} {
	//	t := template.Must(template.ParseFiles(teml + ".html"))
	//	templates[tmpl] = t
	//}
}



