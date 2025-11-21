package gcd

import "testing"

func TestGcd(t *testing.T) {
	expected := 8
	actual := Gcd(56, 48)

	if expected != actual {
		t.Errorf("Expected value: %v, got %v instead", expected, actual)
	}
}
