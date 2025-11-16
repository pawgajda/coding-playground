package factorial

// recursive approach
func Factorial(n int) int {
	if n == 0 {
		return 1
	} else {
		return n * Factorial(n-1)
	}
}

// iterative apprach
func FactorialIterative(n int) int {
	factorial := 1
	for ; n > 0; n-- {
		factorial *= n
	}
	return factorial
}
