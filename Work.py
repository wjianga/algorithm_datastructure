#  File: Work.py

#  Description: using both linear and binary search to find the minimum lines of code to start with

#  Student Name: Wenxuan Jiang

#  Student UT EID: wj3972

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 02/19/2021

#  Date Last Modified: 02/19/2021

import sys

import time

# Input: v an integer representing the minimum lines of code and
#        k an integer representing the productivity factor
# Output: computes the sum of the series (v + v // k + v // k**2 + ...)
#         returns the sum of the series
def sum_series (v, k):
    result = 0
    index = 0

    # Keep adding the writtable lines of code to the results if the lines of code are not 0
    while not v // (k ** index) < 1:
        result += v // (k ** index)
        index += 1
    
    return result

# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using linear search
def linear_search (n, k):
    # Check from 0 to n to see at which start point will the result be above n lines
    for i in range(n):
        if sum_series(i + 1, k) >= n:
            # Return the number of lines at the beginning
            return i + 1

    return -1

# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using binary search
def binary_search (n, k):
    # Declare the maximum and minimum lines of code to start
    max = n
    min = 1
    while min <= max:
        # start from the middle number
        start_lines = (max + min) // 2
        # reuslt is the end number of codes if starting with start_lines
        result = sum_series(start_lines, k)
        # result is less than what is needed
        if result < n:
            min = start_lines + 1

        elif result > n:
            # return the minimum start lines to achieve the goal where you would fail with only one line fewer
            if sum_series(start_lines - 1, k) < n:
                return start_lines
            # if it is not the minimum, reduce the upper bound
            max = start_lines - 1
        
        # return the start_lines if the result matches the goal
        else:
            return start_lines

    return -1

# Input: no input
# Output: a string denoting all test cases have passed
def test_cases():
    # write your own test cases
    assert sum_series(1, 4) == int(4/3)
    assert sum_series(100, 2) == int(200)

    return "all test cases passed"

def main():
  # read number of cases
  line = sys.stdin.readline()
  line = line.strip()
  num_cases = int (line)

  for i in range (num_cases):
    line = sys.stdin.readline()
    line = line.strip()
    inp =  line.split()
    n = int(inp[0])
    k = int(inp[1])

    start = time.time()
    print("Binary Search: " + str(binary_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()

    start = time.time()
    print("Linear Search: " + str(linear_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()
    print()

if __name__ == "__main__":
  main()
