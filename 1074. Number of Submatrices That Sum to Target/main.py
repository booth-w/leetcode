def numSubmatrixSumTarget(matrix, target):
	count = 0
	r, c = len(matrix), len(matrix[0])

	# prefix sum of matrix
	for y in range(r):
		for x in range(1, c):
			matrix[y][x] += matrix[y][x-1]
	for y in range(1, r):
		for x in range(c):
			matrix[y][x] += matrix[y-1][x]

	for y1 in range(r):
		for y2 in range(y1, r):
			prefixSumCount = {0: 1}
			for x1 in range(c):
				currentSum = matrix[y2][x1]
				if y1 > 0:
					currentSum -= matrix[y1-1][x1]
				count += prefixSumCount.get(currentSum - target, 0)
				prefixSumCount[currentSum] = prefixSumCount.get(currentSum, 0) + 1

	return count
