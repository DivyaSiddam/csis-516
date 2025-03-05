import random
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Assume a list is given
for row in range(0, len(matrix)):
for column in range(0, len(matrix[row])):
i = random.randrange(0, len(matrix))
j = random.randrange(0, len(matrix[row]))
# Swap matrix[row][column] with matrix[i][j]
matrix[row][column], matrix[i][j] = \
matrix[i][j], matrix[row][column]
print(matrix)
