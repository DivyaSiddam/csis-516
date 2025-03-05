matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Assume a list is given
total = 0
for row in range(0, len(matrix)):
for column in range(0, len(matrix[row])):
total += matrix[row][column]
print("Total is " + str(total)) # Print the total
