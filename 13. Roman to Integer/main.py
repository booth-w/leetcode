def romanToInt(str):
	roman = {
		"I": 1,
		"V": 5,
		"X": 10,
		"L": 50,
		"C": 100,
		"D": 500,
		"M": 1000
	}

	result = 0

	for a in str:
		result += roman[a]

	if "IV" in str or "IX" in str:
		result -= 2

	if "XL" in str or "XC" in str:
		result -= 20

	if "CD" in str or "CM" in str:
		result -= 200

	return result
