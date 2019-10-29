package diffsquares

// SquareOfSum calculates square of sum of integers up to N
func SquareOfSum(n int) int {
	sum := (1 + n) * n / 2
	return sum * sum
}

// SumOfSquares calculates sum of squares of integers up to N
func SumOfSquares(n int) int {
	return (n * (n + 1) * (2*n + 1)) / 6
}

// Difference calculates difference between square of sum & sum of squares of integers up to N
func Difference(N int) int {
	return SquareOfSum(N) - SumOfSquares(N)
}
