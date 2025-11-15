package linearsearch

func LinearSearch(arr []int, n int) int {
	for i, v := range arr {
		if v == n {
			// return index of n
			return i
		}
	}
	// not found
	return -1
}
