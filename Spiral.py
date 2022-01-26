#  File: Spiral.py

#  Description: Create a number spiral with arbitrary odd dimensions. Sum up adjacent numbers of a target number.

#  Student Name: Wenxuan Jiang

#  Student UT EID: wj3972

#  Partner Name: Zixi Lei

#  Partner UT EID: zl7732

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 01/26/2021

#  Date Last Modified: 01/28/2021

# Input: n is an odd integer between 1 and 100
# Output: returns a 2-D list representing a spiral
#         if n is even add one to n

import sys

def create_spiral(n):

    # n is even
    if n % 2 == 0:  
        n += 1

    # n is odd
    num = n * n
    round_num = int((n-1)/2)

    if n % 2 != 0:
        matrix = [[0] * n for i in range(n)]

       # Declare variables that store times of left fill and the number of steps
        timesOfLeft = 0
        stepOfLeft = n


       # Down
        timesOfDown = 0
        stepOfDown = n - 1

       # Right
        timesOfRight = 0
        stepOfRight = n - 1

       # Up
        timesOfUp = 0
        stepOfUp = n - 2

        for i in range(round_num):
            deRows = n # The number of entries of a row that will decrease
            deCols = n
            inRows = 0 # The number of entries of a row that will increase
            inCols = 0

            # Fill the matrix in a left direction
            for i in range(stepOfLeft):
                matrix[timesOfLeft][deCols - 1 - timesOfLeft] = num
                deCols -= 1
                num -= 1
            timesOfLeft += 1
            stepOfLeft -= 2

            # Down
            for i in range(stepOfDown):
                matrix[inRows + 1 + timesOfDown][timesOfDown] = num
                inRows += 1
                num -= 1
            timesOfDown += 1
            stepOfDown -= 2

            # Right
            for i in range(stepOfRight):
                matrix[n - 1 - timesOfRight][inCols + timesOfRight + 1] = num
                inCols += 1
                num -= 1
            timesOfRight += 1
            stepOfRight -= 2

            # Up
            for i in range(stepOfUp):
                matrix[deRows - 2 - timesOfUp][n - 1 - timesOfUp] = num
                deRows -= 1
                num -= 1
            timesOfUp += 1
            stepOfUp -= 2

        # Fill in the middle entry with number 1
        matrix[round_num][round_num]=1

    return matrix


# Input: spiral is a 2-D list and n is an integer
# Output: returns an integer that is the sum of the
#         numbers adjacent to n in the spiral
#         if n is outside the range return 0

def sum_adjacent_numbers (spiral, n):
    
    # Store the length of a matrix, or dimensions
    matrix_len = len(spiral[0])

    # Target number is outside the range
    if n > matrix_len ** 2:
        return 0

    # Find the first index
    first_index = 0

    for i in range(len(spiral)):
        if n in spiral[i]:
            first_index += i
    
    # Find the Second index
    second_index = spiral[first_index].index(n)

    sumOutput = 0

    # Get the indices of eight numbers around the target number and add them up
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            # Exclude the target number itself
            if (i == 0 and j == 0):
                sumOutput += 0
            # Takes care of the adjacent numbers outsides the outer circle of the matrix
            elif (first_index + i < 0 or first_index + i > matrix_len - 1 or
            second_index + j < 0 or second_index + j > matrix_len - 1):
                sumOutput += 0
            else:
                sumOutput += spiral[first_index + i][second_index + j]
    
    return sumOutput


def main():
    
    # Read the input file
    inputFile = sys.stdin.read().strip().split("\n")

    # Create the spiral
    spiral = create_spiral(int(inputFile[0]))

    # Add the adjacent numbers and print the result
    for i in range(1, len(inputFile)):
        print(sum_adjacent_numbers (spiral, int(inputFile[i])))


if __name__ == "__main__":
   main()
