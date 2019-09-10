package strain

// Ints is an array of Ints
type Ints []int

// Lists is an 2D array of Ints
type Lists [][]int

// Strings is an array of strings
type Strings []string

type pred func(int) bool

// Discard returns a new collection containing those elements where the predicate is false
func (slice Ints) Discard(fn pred) (out Ints) {
	for _, item := range slice {
		if !fn(item) {
			out = append(out, item)
		}
	}
	return
}

// Keep returns a new collection containing those elements where the predicate is true
func (slice Ints) Keep(fn pred) (out Ints) {
	for _, item := range slice {
		if fn(item) {
			out = append(out, item)
		}
	}
	return
}

// Keep returns a new collection containing those elements where the predicate is true
func (slice Strings) Keep(fn func(string) bool) (out Strings) {
	for _, item := range slice {
		if fn(item) {
			out = append(out, item)
		}
	}
	return
}

// Keep returns a new collection containing those elements where the predicate is true
func (slice Lists) Keep(fn func([]int) bool) (out Lists) {
	for _, item := range slice {
		if fn(item) {
			out = append(out, item)
		}
	}
	return
}
