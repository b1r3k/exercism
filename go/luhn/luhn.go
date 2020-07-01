package luhn

//package main

import (
	//"fmt"
	"strconv"
	"strings"
	"unicode"
)

// Valid verifies Luhn code
func Valid(input string) bool {
	var cardNumberDigits []int
	cardNumber := strings.Replace(input, " ", "", -1)
	for _, char := range cardNumber {
		if unicode.IsNumber(char) {
			num, err := strconv.Atoi(string(char))
			if err == nil {
				cardNumberDigits = append(cardNumberDigits, num)
			}
		} else {
			return false
		}
	}
	if len(cardNumberDigits) <= 1 {
		return false
	}
	sumDigits := cardNumberDigits

	for i := len(cardNumberDigits) - 2; i >= 0; i -= 2 {
		sumDigits[i] = cardNumberDigits[i] * 2
		if sumDigits[i] > 9 {
			sumDigits[i] = sumDigits[i] - 9
		}
	}
	//fmt.Println("Sum digits", sumDigits)
	sum := 0
	for _, x := range sumDigits {
		sum += x
	}
	return sum%10 == 0
}

//func main() {
//	Valid("059")
//}
