package linearsearch

import (
	"testing"
)

func TestSearchSuccess(t *testing.T) {
	// define example array of integers
	arr := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}

	// index of 15
	expected := 14
	actual := LinearSearch(arr, 15)

	if actual != expected {
		t.Errorf("Expected index %d, got %d", expected, actual)
	}
}

func TestSearchFailure(t *testing.T) {
	// define example array of integers
	arr := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}

	// look for value that does not exist in the array
	expected := -1
	actual := LinearSearch(arr, 256)

	if actual != expected {
		t.Errorf("Expected index %d, got %d", expected, actual)
	}
}

func TestSearchEmptyArray(t *testing.T) {
	// define empty array
	arr := []int{}

	expected := -1
	actual := LinearSearch(arr, 128)

	if actual != expected {
		t.Errorf("Expected index %d, got %d", expected, actual)
	}

}
