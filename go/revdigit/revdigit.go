package revdigit

func ReverseDigits(num int) int {
	rev := 0
	r := 0
	tmp := num

	for tmp > 0 {
		r = tmp % 10
		rev = rev*10 + r
		tmp = tmp / 10
	}
	return rev
}
