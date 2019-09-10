package triangle

import "math"

type Kind int

const (
	// Pick values for the following identifiers used by the test program.
	NaT Kind = 0 // not a triangle
	Equ Kind = 1 // equilateral
	Iso Kind = 2 // isosceles
	Sca Kind = 3 // scalene
)

func KindFromSides(a, b, c float64) Kind {
	if a <= 0 || b <= 0 || c <= 0 {
		return NaT
	}
	if math.IsNaN(a) || math.IsNaN(b) || math.IsNaN(c) || math.IsInf(a, 0) || math.IsInf(b, 0) || math.IsInf(c, 0) {
		return NaT
	}
	if a+b < c || a+c < b || b+c < a {
		return NaT
	}
	if a == b && b == c && c == a {
		return Equ
	}
	if a == b || a == c || b == c {
		return Iso
	}
	if a != b && a != c && c != b {
		return Sca
	}
	return NaT
}
