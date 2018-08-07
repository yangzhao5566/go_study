package make

import "log"

func makeThumbnails6(filenames <-chan string) int {
	sizes := make(chan int64)
	var wg sync.WaitGroup
	for f := range filenames {
		wg.Add(1)
		go func(s string) {
			defer wg.Done()  // 等待执行完以后wg减1
			thumb, err := thumbnail.ImageFile(f)
			if err != nil {
				log.Println(err)
				return
			}
			info, _ := os.Stat(thumb)
			sizes <- info.Size()
		}(f)
	}

	go func() {
		wg.Wait()  // 当上边执行完以后 关闭channel
		close(sizes)
	}()

	var total int64
	for size := range sizes {
		total += size
	}
	return total  // 计算总的size大小
}