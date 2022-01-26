#  File: Triangle.py

#  Description: find the greatest path sum starting at the top of the triangle and
#  moving only to adjacent numbers on the row below

#  Student Name: Zixi Lei

#  Student UT EID: zl7732

#  Partner Name: Wenxuan Jiang

#  Partner UT EID: wj3972

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 03/24/21
 
#  Date Last Modified: 03/24/21

import sys

from timeit import timeit

# brute force helper function
# the sum up to the current line is already calculated and included in the parameter, every function call is to include the numbers in the next line
def brute_force_helper(grid, line, idx, sum, sum_list):
    # base case: when it reaches the last line, append the sum, included in the parameter to sum_list
    if line == len(grid) - 1:
        sum_list.append(sum)
    else:
        # recursive case:
        # add the element on the left side in the next line
        brute_force_helper(grid, line + 1, idx, sum + grid[line + 1][idx], sum_list)
        # add the element on the right side in the next line
        brute_force_helper(grid, line + 1, idx + 1, sum + grid[line + 1][idx + 1], sum_list)

# returns the greatest path sum using exhaustive search
def brute_force (grid):
    sum_list = []
    brute_force_helper(grid, 0, 0, grid[0][0], sum_list)

    return max(sum_list)

# returns the greatest path sum using greedy approach
def greedy (grid):
    # set the initial max_value to be the maximum number of the first line
    max_value = grid[0][0]
    # set the initial max_sum
    max_sum = grid[0][0]
    # set the current index
    idx = 0
    # loop through the 2-D lists
    for i in range(len(grid)-1):
        # if the left number is greater than the right, set the max_value to be the left one
        # also add the number to the max_sum
        if grid[i+1][idx] > grid[i+1][idx+1]:
            max_sum += grid[i+1][idx]
            max_value = grid[i+1][idx]
        # vice versa
        else:
            max_sum += grid[i+1][idx + 1]
            max_value = grid[i+1][idx + 1]
            idx = idx + 1

    return max_sum

# divide and conquer helper function
# each number is a function call
def divide_conquer_helper(grid, line, idx):
    # if call reaches the second last line, select the maximum number in the last line and sum up with itself
    if line == len(grid) - 2:
        return grid[line][idx] + max(grid[line + 1][idx], grid[line + 1][idx + 1])
    # for every other number, do the same as in the base case
    else:
        return grid[line][idx] + max(divide_conquer_helper(grid, line + 1, idx), divide_conquer_helper(grid, line + 1, idx + 1))
        
# returns the greatest path sum using divide and conquer (recursive) approach
def divide_conquer (grid):
    return divide_conquer_helper(grid, 0, 0)

# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog (grid):
    new_grid = grid[:][:]
    # starting from the second last line, replace the entry in new_grid with the greatest possible sum
    for i in range(len(grid) - 2, -1, -1):
        for j in range(i + 1):
            new_grid[i][j] = grid[i][j] + max(new_grid[i + 1][j], new_grid[i + 1][j + 1])

    return new_grid[0][0]

# reads the file and returns a 2-D list that represents the triangle
def read_file ():
  # read number of lines
  line = sys.stdin.readline()
  line = line.strip()
  n = int (line)

  # create an empty grid with 0's
  grid = [[0 for i in range (n)] for j in range (n)]

  # read each line in the input file and add to the grid
  for i in range (n):
    line = sys.stdin.readline()
    line = line.strip()
    row = line.split()
    row = list (map (int, row))
    for j in range (len(row)):
      grid[i][j] = grid[i][j] + row[j]

  return grid 

def main ():
    # read triangular grid from file
    grid = read_file()

    # check that the grid was read in properly

    # output greatest path from exhaustive search
    print("The greatest path sum through exhaustive search is")
    print(brute_force(grid))
    
    times = timeit ('brute_force({})'.format(grid), 'from __main__ import brute_force', number = 10)
    times = times / 10
    # print time taken using exhaustive search
    print(times)

    # output greatest path from greedy approach
    print("The greatest path sum through greedy search is ")
    print(greedy(grid))

    times = timeit ('greedy({})'.format(grid), 'from __main__ import greedy', number = 10)
    times = times / 10
    # print time taken using greedy approach
    print(times)

    # output greatest path from divide-and-conquer approach
    print("The greatest path sum through recursive search is")
    print(divide_conquer(grid))

    times = timeit ('divide_conquer({})'.format(grid), 'from __main__ import divide_conquer', number = 10)
    times = times / 10
    # print time taken using divide-and-conquer approach
    print(times)

    # output greatest path from dynamic programming 
    print("The greatest path sum through dynamic programming is")
    print(dynamic_prog(grid))

    times = timeit ('dynamic_prog({})'.format(grid), 'from __main__ import dynamic_prog', number = 10)
    times = times / 10
    # print time taken using dynamic programming
    print(times)

if __name__ == "__main__":
  main()

