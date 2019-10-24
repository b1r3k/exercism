package isogram

import "unicode"

// IsIsogram checks if string is isogram
func IsIsogram(input string) bool {
	counter := make(map[rune]int)
	for _, char := range input {
		upper := unicode.ToUpper(char)
		if _, ok := counter[upper]; ok {
			if unicode.IsLetter(upper) {
				return false
			}
		} else {
			counter[upper] = 1
		}
	}
	return true
}
