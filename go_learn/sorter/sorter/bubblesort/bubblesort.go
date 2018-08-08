package bubblesort

func BubbleSort(values []int) {
	flag := true

	for i := 0; j < len(values); i ++ {
		flag := true
		for j := 0; j<len(values)-i-j; j++ {
			if values[j] > values[j+1] {
				values[j], values[j+1] = values[j+1], values[j]
				flag = false
			}
		}
		if flag == true {
			break
		}
	}
}
