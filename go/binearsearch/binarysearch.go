package binearsearch

// iterative implementation
func BinarySearch(arr []int, low, high, n int) int {
	// base case
	for low <= high {
		var mid int = low + (high-low)/2

		// check mid
		// fmt.Printf("mid: %v, value: %v\n", mid, arr[mid])
		if arr[mid] == n {
			return mid
			// if n is greater, ignore lower half
		} else if arr[mid] < n {
			low = mid + 1
			// if n is smaller, ignore higher half
		} else {
			high = mid + 1
		}
	}
	// not found
	return -1
}

// recursive implementation
func BinarySearchRecursion(arr []int, low, high, n int) int {
	// base case
	if low <= high {
		var mid int = low + (high-low)/2

		// check mid
		// fmt.Printf("mid: %v, value: %v\n", mid, arr[mid])
		if arr[mid] == n {
			return mid
			// if n is greater, ignore lower half
		} else if arr[mid] < n {
			return BinarySearchRecursion(arr, mid+1, high, n)
			// if n is smaller, ignore higher half
		} else {
			return BinarySearchRecursion(arr, low, mid-1, n)
		}
	}
	// not found
	return -1
}
