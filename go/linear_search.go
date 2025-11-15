package main

import (
	"fmt"
)

func linear_search(arr []int, n int) int {
	for i, v := range arr {
		if v == n {
			// return index of n
			return i
		}
	}
	// not found
	return -1
}

func main() {
	// define example array of integers
	arr := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}

	// test for success
	n := 15
	result := linear_search(arr, n)
	fmt.Printf("Linear Search for number %v: %v\n", n, result)

	// test for failure
	n = 25
	result = linear_search(arr, n)
	fmt.Printf("Linear Search failure for number %v: %v\n", n, result)
}
