package revdigit

import "testing"

func TestRevDigit(t *testing.T) {
	number := 456
	expected := 654

	actual := ReverseDigits(number)
	t.Logf("Reverse digits for number %v, result %v", number, actual)

	if expected != actual {
		t.Errorf("Reverse digits for number %v, expected %v, got %v", number, expected, actual)
	}

}
