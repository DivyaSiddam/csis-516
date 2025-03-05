matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Assume a list is given
maxRow = sum(matrix[0]) # Get sum of the first row in maxRow
indexOfMaxRow = 0
for row in range(1, len(matrix)):
if sum(matrix[row]) > maxRow:
maxRow = sum(matrix[row])
indexOfMaxRow = row
print("Row " + str(indexOfMaxRow)
