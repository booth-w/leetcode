def primePalindrome(n):
	if n == 1:
		return 2
	while True:
		if str(n) == str(n)[::-1] and all(n % a != 0 for a in range(2, int(n ** 0.5) + 1)):
			return n
		n += 1
		if 10**7 < n < 10**8:
			n = 10**8
