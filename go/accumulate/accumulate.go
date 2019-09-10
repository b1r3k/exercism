package accumulate

type converter func(string) string

// Accumulate converts list of string items using provided converter function
func Accumulate(items []string, fn converter) []string {
	var accumulated = make([]string, len(items))
	for idx, item := range items {
		accumulated[idx] = fn(item)
	}
	return accumulated
}
