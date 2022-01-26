#  File: Intervals.py

#  Description: Take a set of intervals and collapse all the overlapping intervals
#  and print the smallest set of non-intersecting intervals in ascending order
#  of the lower end of the interval and then print the intervals
#  in increasing order of the size of the interval.

#  Student Name: Zixi Lei

#  Student UT EID: zl7732

#  Partner Name: Wenxuan Jiang

#  Partner UT EID: wj3972

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 01/30/2021

#  Date Last Modified: 02/03/2021

import sys

#Function to create a list of tuples from inputfiles
def create_tuple_list(inputFile):
   tuple_list = []
   list_length = int(inputFile[0])

   #Read in the line
   for i in range(1, list_length + 1 ):
      line = inputFile[i].split()
      tuple_list.append((int(line[0]),int(line[1])))

   return tuple_list

# Input: tuples_list is an unsorted list of tuples denoting intervals
# Output: a list of merged tuples sorted by the lower number of the
#         interval

def merge_tuples(tuples_list):
   output = []

   # Convert the tuple lists to a 2d list and sort in ascending order
   work_list = [list(i) for i in tuples_list]
   work_list.sort()

   # Append the first tuple in the output list to compare
   output.append(work_list[0])

   # Search for intersections between the last element in the output list
   # and the tuples in the ascending-sorted list
   for i in range(1, len(work_list)):

      # Intersection found
      if output[-1][1] >= work_list[i][0]:
         # The second intersected interval is a subset of the first interval
         if work_list[i][1] <= output[-1][1]:
            continue
         # Merge two intervals if their union is larger
         else:
            output[-1][1] = work_list[i][1]

      # No intersections found
      # Append the list from work_list to output list as reference
      else:
         output.append(work_list[i])

   # Convert the 2d list back to a tuple list
   tuples_list = [tuple(i) for i in output]

   return tuples_list


# Input: tuples_list is a list of tuples of denoting intervals
# Output: a list of tuples sorted by ascending order of the size of
#         the interval
#         if two intervals have the size then it will sort by the
#         lower number in the interval
def sort_by_interval_size(tuples_list):
   # Sort in ascending order of their lower ends and by the size of the intervals
   tuples_list.sort(key=lambda x: [x[1] - x[0], x[0]])
   return tuples_list


# Input: no input
# Output: a string denoting all test cases have passed
def test_cases ():
   assert merge_tuples([(1,2)]) == [(1,2)]
   # write your own test cases
   assert merge_tuples([(1,5), (2, 7), (6, 10), (8, 100)]) == [(1, 100)]

   assert sort_by_interval_size([(1,3), (4,5)]) == [(4,5), (1,3)]
   # write your own test cases
   assert sort_by_interval_size([(1, 100), (50, 150), (100, 200)]) == [(1, 100), (50, 150), (100, 200)]

   return "all test cases passed"


def main():
   # open file intervals.in and read the data and create a list of tuples
   inputFile = sys.stdin.read().strip().split("\n")
   create_list = create_tuple_list(inputFile)

   # merge the list of tuples
   merged_list = merge_tuples(create_list)

   # sort the list of tuples according to the size of the interval
   merged_list_sort = merge_tuples(create_list)
   sorted_output = sort_by_interval_size(merged_list_sort)

   # run your test cases
   """
   print(test_cases())
   """

   # open file intervals.out and write the output list of tuples
   # from the two functions
   print(merged_list)
   print(sorted_output)


if __name__ == "__main__":
   main()

