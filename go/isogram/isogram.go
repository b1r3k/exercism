package isogram

import "unicode"

// IsIsogram checks if string is isogram
func IsIsogram(input string) bool {
	counter := make(map[rune]int)
	for _, char := range input {
		if !unicode.IsLetter(char) {
			continue
		}
		upper := unicode.ToUpper(char)
		if _, ok := counter[upper]; !ok {
			counter[upper] = 1
		} else {
			return false
		}
	}
	return true
}
