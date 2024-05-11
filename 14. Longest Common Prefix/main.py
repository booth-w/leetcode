def longestCommonPrefix(strs):
	if not strs:
		return ""

	shortest = min(strs, key=len)
	for a, char in enumerate(shortest):
		for b in strs:
			if b[a] != char:
				return shortest[:a]
				
	return shortest

print(longestCommonPrefix(["flower", "flow", "flight"])) # "fl"