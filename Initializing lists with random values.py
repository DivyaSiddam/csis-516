import random
matrix = [] # Create an empty list
numberOfRows = eval(input("Enter the number of rows: "))
numberOfColumns = eval(input("Enter the number of columns: "))
for row in range(0, numberOfRows):
matrix.append([]) # Add an empty new row
for column in range(0, numberOfColumns):
matrix[row].append(random.randrange(0, 100))
print(matrix)
