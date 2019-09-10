package etl

import "strings"

//Transform transforms the legacy data format to the shiny new format.
func Transform(s map[int][]string) map[string]int {
	var transformed = make(map[string]int)
	for score, letters := range s {
		for i := 0; i < len(letters); i++ {
			letter := strings.ToLower(letters[i])
			transformed[letter] = score
		}
	}
	return transformed
}
