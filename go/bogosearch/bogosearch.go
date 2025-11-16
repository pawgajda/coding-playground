package bogosearch

import (
	"math/rand/v2"
	"time"
)

func BogoSearch(arr []int, n, maxTries int, rng *rand.Rand) (int, int) {
	// set default maxTries
	if maxTries == -1 {
		maxTries = 9999
	}

	// fallback if Rand is not provided
	if rng == nil {
		seed := time.Now().UnixNano()
		// int64 needs to be converted to uint64 for NewPCG function
		rng = rand.New(rand.NewPCG(uint64(seed), 0))
	}

	// initialize number of tries
	tries := 0

	// handle empty array earlier
	if len(arr) == 0 {
		return -1, tries
	}

	// search for number
	for tries < maxTries {
		index := rng.IntN(len(arr))
		tries += 1

		if arr[index] == n {
			return index, tries
		}
	}
	// not found
	return -1, tries
}
