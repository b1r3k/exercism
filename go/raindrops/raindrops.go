package raindrops

import "math"
import "strconv"

// Convert takes integer and converts it to a string according to rules
func Convert(n int) string {
	var output = ""
	if math.Mod(float64(n), 3) == 0 {
		output += "Pling"
	}
	if math.Mod(float64(n), 5) == 0 {
		output += "Plang"
	}
	if math.Mod(float64(n), 7) == 0 {
		output += "Plong"
	}
	if len(output) == 0 {
		return strconv.Itoa(n)
	}
	return output
}
