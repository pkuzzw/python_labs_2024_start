# Create a list of fruits
fruits = ['apple', 'banana', 'cherry']

# Print the list
print(fruits)

# Print the first item in the list
print(fruits[0])

# Print the last item in the list
print(fruits[-1])

# Print the length of the list
print(len(fruits))

# Add an item to the end of the list
fruits.append('date')
print(fruits)

# Remove an item from the list
fruits.remove('banana')
print(fruits)

# Remove an item from the list by index
del fruits[0]
print(fruits)

# Remove the last item from the list
fruits.pop()
print(fruits)

# Remove all items from the list
fruits.clear()
print(fruits)

# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Print the list
print(numbers)

# Print the first three items in the list
print(numbers[:3])

# Print the last two items in the list
print(numbers[-2:])

# Print the sum of the list
print(sum(numbers))

# Print the maximum value in the list
print(max(numbers))

# Print the minimum value in the list
print(min(numbers))

# Print the average value in the list
print(sum(numbers) / len(numbers))

# Create a list of lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Print the list
print(matrix)

# Print the first item in the list
print(matrix[0])

# Print the first item in the first list
print(matrix[0][0])

# Print the last item in the last list
print(matrix[-1][-1])

# Print the length of the list
print(len(matrix))

# Print the sum of the list
print(sum(matrix[0]))

# Print the sum of the list
print(sum(matrix[1]))

# Print the sum of the list
print(sum(matrix[2]))

# Print the sum of the list
print(sum(matrix[0]) + sum(matrix[1]) + sum(matrix[2]))

# Print the sum of the list
print(sum(sum(matrix, [])))
      
      