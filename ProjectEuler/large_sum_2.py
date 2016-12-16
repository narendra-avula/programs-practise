__author__ = 'narendra'

# Read the problem matrix into an array in python
filename = 'euler13.txt'

with open(filename, "r") as ins:
    array = []
    for line in ins:
        array.append(line)
    print array

# Convert the array into an array of integers
newArray = []
for i in array:
    newArray.append(int(i))
print newArray

# Sum up the array and print the first 10 numbers of the sum as a string
# arraySum = sum(newArray)
# print str(arraySum)[:10]