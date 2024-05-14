import re

def isPalindrome(s):
	s = re.sub(r"[^a-zA-Z0-9]", "", s).lower()
	return s == s[::-1]