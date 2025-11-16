package factorial

import "testing"

func TestFactorialZero(t *testing.T) {
	expected := 1
	actual := Factorial(0)

	if expected != actual {
		t.Errorf("Expected %d, got %d", expected, actual)
	}
}

func TestFactorial(t *testing.T) {
	expected := 120
	actual := Factorial(5)

	if expected != actual {
		t.Errorf("Expected %d, got %d", expected, actual)
	}
}

func TestFactorialZeroIterative(t *testing.T) {
	expected := 1
	actual := FactorialIterative(0)

	if expected != actual {
		t.Errorf("Expected %d, got %d", expected, actual)
	}
}

func TestFactorialIterative(t *testing.T) {
	expected := 120
	actual := FactorialIterative(5)

	if expected != actual {
		t.Errorf("Expected %d, got %d", expected, actual)
	}
}
