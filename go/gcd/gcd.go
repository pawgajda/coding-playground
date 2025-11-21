package gcd

// Greatest Common Divisor
func Gcd(a, b int) int {
	// keep looking for GCD until remainder of a / b equals 0
	for b != 0 {
		// calculate the remainder of a / b
		r := a % b
		// swap values of a with b and b with division remainder
		a = b
		b = r
	}
	return a
}
