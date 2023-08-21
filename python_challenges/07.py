# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i _ j.*
# Note: i=0,1.., X-1; j=0,1,¡­Y-1. Suppose the following inputs are given to the program: 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
ij = input('Please enter the i and j separated by a comma: ')
input_array = ij.split(',')
input_array_int = [int(x) for x in input_array]
result_array = []
temp_array = []
for i in range(0, input_array_int[0]):
    for j in range(0, input_array_int[1]):
        temp_array.append(i*j)
    result_array.append(temp_array)
    temp_array = []
print(result_array)
