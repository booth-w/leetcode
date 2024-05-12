def largestLocal(grid):
	n = len(grid) - 2
	gridNew = [[0]*n for b in range(n)]

	for a in range(1, len(grid) - 1):
		for b in range(1, len(grid) - 1):
			gridNew[a - 1][b - 1] = max(grid[aa][bb] for aa in range(a-1, a+2) for bb in range(b-1, b+2))

	return gridNew
