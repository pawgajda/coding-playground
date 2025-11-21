package lcm

import "testing"

func TestLcm(t *testing.T) {
	expected := 42
	actual := Lcm(21, 6)

	if expected != actual {
		t.Errorf("Expected value: %v, got %v instead", expected, actual)
	}
}
