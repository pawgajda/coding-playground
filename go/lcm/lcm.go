package lcm

import (
	"math"
	"pawgajda/coding-playground/gcd"
)

// Least Common Multiple using GCD
func Lcm(a, b int) int {
	// get absolute values of a and b
	a = int(math.Abs(float64(a)))
	b = int(math.Abs(float64(b)))

	result := a * b / gcd.Gcd(a, b)
	return result
}
