package fizzbuzz

import "testing"

func TestFizzBuzz(t *testing.T) {
	expected := "FizzBuzz"
	// 30 / 3 = 10, 30 / 5 = 6 gives FizzBuzz
	actual := FizzBuzz(30)

	if expected != actual {
		t.Errorf("Expected %s, got %s", expected, actual)
	}
}

func TestFizz(t *testing.T) {
	expected := "Fizz"
	// 99 / 3 = 33 gives 'Fizz'
	actual := FizzBuzz(99)

	if expected != actual {
		t.Errorf("Expected %s, got %s", expected, actual)
	}
}

func TestBuzz(t *testing.T) {
	expected := "Buzz"
	// 55 / 5 = 11 gives 'Buzz'
	actual := FizzBuzz(55)

	if expected != actual {
		t.Errorf("Expected %s, got %s", expected, actual)
	}
}

func TestFailure(t *testing.T) {
	// must be a string
	expected := "11"
	// 11 is not divisible by 3 or 5, returns a number as string
	actual := FizzBuzz(11)

	if expected != actual {
		t.Errorf("Expected %s, got %s", expected, actual)
	}
}
