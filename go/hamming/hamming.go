package hamming

import (
	"errors"
)

// Distance calculates hamming distance between to DNA sequences represented by strings
func Distance(a, b string) (int, error) {
	if len(a) != len(b) {
		return 0, errors.New("unequal sequences")
	}
	distance := 0
	for i := 0; i < len(a); i++ {
		if a[i] != b[i] {
			distance++
		}
	}
	return distance, nil
}
