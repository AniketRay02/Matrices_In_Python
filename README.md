# Matrices_In_Python

A python script to compute basic matrix operations. Below are the explanation for each function

Transpose - This function should take a matrix and create a new matrix where the columns and rows are flipped so if you were to have an input of 2x3 matrix, the output would be 3x2

Powers - This function should take a list and two numbers as an input and then compute a matrix. For each number in the list, it shall create one row with the powers of the original number. For example, if the first number in the list is 3 and the two other arguments of the function are 0 and 2, the corresponding row should be [1, 3, 9] which is equal to [3 ** 0, 3 ** 1, 3 ** 2]. 

Matmul - This function multiplies two matrices with each other. It also works nicely if you mulitply a normal matrix with the unix matrix if you're interested.

Invert - This function should take  square matrix and computer another square matrix such that matmul(A,invert(A)) is always the unit matrix. 

loadtxt - this function takes as an argument the name of a file. The file should contain several lines, where each line contains space-separated numbers. 

To run a specific function you'd write it in your terminal:

>>>from matrix import matmul
>>>matmul([[1, 2, 3], [4, 5, 6]],[[7,8,9,10],[11,12,13,14],[15,16,17,18]])

The expected answer would be 
[[74, 80, 86, 92], [173, 188, 203, 218]] 
if everything is ran correctly
