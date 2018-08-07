package main


type PersionInfo struct {
	ID string
	Name string
	Address string
}

func main() {
	var personDB map[string] PersionInfo
	personDB = make(map[string] PersionInfo)
	personDB["12345"] = PersionInfo{"12345", "Tom", "Room 203, ..."}
	personDB["1"] = PersionInfo{"1","Jack", "Room 101,..."}
	person, ok := personDB["12345"]
	if ok {
		fmt.Println("Found person", person.Name, "with ID 1234.")
	} else {
		fmt.Println("Did not find person with ID 1234.")
	}
}
