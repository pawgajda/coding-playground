package bogosearch

import (
	"math/rand/v2"
	"testing"
)

const SEED uint64 = 768
const MAXTRIES int = 9999

func TestBogoSearchSuccess(t *testing.T) {
	// define Rand with SEED
	rng := rand.New(rand.NewPCG(SEED, 0))

	// define example array of integers
	arr := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}

	// index of 15
	expected := 14

	expectedTries := 3
	actual, actualTries := BogoSearch(arr, 15, MAXTRIES, rng)

	t.Logf("Execution took %d tries", actualTries)

	if actual != expected {
		t.Errorf("Expected index %d, got %d", expected, actual)
	}

	if actualTries != expectedTries {
		t.Errorf("Expected tries %d, got %d instead", expectedTries, actualTries)
	}
}

func TestBogoSearchFailure(t *testing.T) {
	// define Rand with SEED
	rng := rand.New(rand.NewPCG(SEED, 0))

	// define example array of integers
	arr := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}

	// not found
	expected := -1

	expectedTries := MAXTRIES
	actual, actualTries := BogoSearch(arr, 256, MAXTRIES, rng)

	t.Logf("Execution took %d tries", actualTries)

	if actual != expected {
		t.Errorf("Expected index %d, got %d", expected, actual)
	}

	if actualTries != expectedTries {
		t.Errorf("Expected tries %d, got %d instead", expectedTries, actualTries)
	}
}

func TestBogoSortEmptyArray(t *testing.T) {
	// define Rand with SEED
	rng := rand.New(rand.NewPCG(SEED, 0))

	// define empty array
	arr := []int{}

	// not found
	expected := -1

	expectedTries := 0
	actual, actualTries := BogoSearch(arr, 128, MAXTRIES, rng)

	t.Logf("Execution took %d tries", actualTries)

	if actual != expected {
		t.Errorf("Expected index %d, got %d", expected, actual)
	}

	if actualTries != expectedTries {
		t.Errorf("Expected tries %d, got %d instead", expectedTries, actualTries)
	}
}

func TestBogoSortRandomArray(t *testing.T) {
	// define Rand with SEED
	rng := rand.New(rand.NewPCG(SEED, 0))

	// 257 elements of values from 0 to 256 in random order
	arr := rng.Perm(257)

	// index of 128
	expected := 161

	expectedTries := 174
	actual, actualTries := BogoSearch(arr, 128, MAXTRIES, rng)

	t.Logf("Execution took %d tries", actualTries)

	if actual != expected {
		t.Errorf("Expected index %d, got %d", expected, actual)
	}

	if actualTries != expectedTries {
		t.Errorf("Expected tries %d, got %d instead", expectedTries, actualTries)
	}
}
