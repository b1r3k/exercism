package isogram

import "strings"

// IsIsogram checks if string is isogram
func IsIsogram(in string) bool {
	counter := make(map[rune]int)
	for _, char := range strings.ToUpper(in) {
		if _, ok := counter[char]; ok {
			counter[char]++
		} else {
			counter[char] = 1
		}
	}
	for char, count := range counter {
		if count > 1 && char != ' ' && char != '-' {
			return false
		}
	}
	return true
}
