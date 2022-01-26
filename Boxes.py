#  File: Boxes.py

#  Description: compute the number of nested boxes and the number of subsets that have such nested boxes

#  Student Name: Zixi Lei

#  Student UT EID: zl7732

#  Partner Name: Wenxuan Jiang

#  Partner UT EID: wj3972

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 03/22/21

#  Date Last Modified: 03/24/2021

import sys
import math

# generates all subsets of boxes and stores them in all_box_subsets
# box_list is a list of boxes that have already been sorted
# sub_set is a list that is the current subset of boxes
# idx is an index in the list box_list
# all_box_subsets is a 3-D list that has all the subset of boxes
def sub_sets_boxes (box_list, sub_set, idx, all_box_subsets):
  # base case: append this subset scenario to all_box_subsets list
  if idx == len(box_list):
    all_box_subsets.append(sub_set)
  else:
    # recursive case:
    # case that does not include the current element
    c = sub_set[:]
    # case that appends the current elelement
    sub_set.append(box_list[idx])
    sub_sets_boxes(box_list, sub_set, idx + 1, all_box_subsets) # case that appends the current elelement
    sub_sets_boxes(box_list, c, idx + 1, all_box_subsets) # case that does not include the current element


# goes through all the subset of boxes and only stores the
# largest subsets that nest in the 3-D list all_nesting_boxes
# largest_size keeps track what the largest subset is
def largest_nesting_subsets (all_box_subsets):
  # keep record of the largest nested boxes
  largest_nested_boxes = 1
  # number of subsets that have the largest nested boxes
  subsets_largerest = 1
  # global variable used to check whether a subset is nested
  check_nested = 1

  for i in range(len(all_box_subsets)): # every all_box_subsets[i] is a 2-D list that is a subset of box list
    # discard the subsets that are equal to 1 or shorter than the current largest subset
    if len(all_box_subsets[i]) < largest_nested_boxes or len(all_box_subsets[i]) == 1: 
      continue

    for j in (range(len(all_box_subsets[i]) - 1)): # all_box_subsets[i][j] is a 1-D list that is the individual box
      if does_fit(all_box_subsets[i][j], all_box_subsets[i][j + 1]):
        check_nested += 1
      else:
        continue
    
    # all boxes in a subsets are nested
    if check_nested == len(all_box_subsets[i]):
      # change the largest size of subsets and its number if the current nested subset is greater than largest_nested_boxes
      if len(all_box_subsets[i]) > largest_nested_boxes:
        subsets_largerest = 1
        largest_nested_boxes = len(all_box_subsets[i])
      # increment the number of subsets with such size if the current subset is equal to what we have so far
      else:
        subsets_largerest += 1 
    
    # reset check_nested for next subset
    check_nested = 1

  # take care of cases when there are no nested boxes
  if largest_nested_boxes == 1 and subsets_largerest == 1:
    subsets_largerest = int(math.log(len(all_box_subsets), 2))
    
  print(largest_nested_boxes)
  print(subsets_largerest)

# returns True if box1 fits inside box2
def does_fit (box1, box2):
  return (box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2])

def main():
  # read the number of boxes 
  line = sys.stdin.readline()
  line = line.strip()
  num_boxes = int (line)

  # create an empty list for the boxes
  box_list = []

  # read the boxes from the file
  for i in range (num_boxes):
    line = sys.stdin.readline()
    line = line.strip()
    box = line.split()
    for j in range (len(box)):
      box[j] = int (box[j])
    box.sort()
    box_list.append (box)

  '''
  # print to make sure that the input was read in correctly
  print (box_list)
  print()
  '''

  # sort the box list
  box_list.sort()

  '''
  # print the box_list to see if it has been sorted.
  print (box_list)
  print()
  '''


  # create an empty list to hold all subset of boxes
  all_box_subsets = []

  # create a list to hold a single subset of boxes
  sub_set = []

  # generate all subsets of boxes and store them in all_box_subsets
  sub_sets_boxes (box_list, sub_set, 0, all_box_subsets)

  # all_box_subsets should have a length of 2^n where n is the number
  # of boxes
  #print(all_box_subsets)

  # go through all the subset of boxes and only store the
  # largest subsets that nest in all_nesting_boxes
  all_nesting_boxes = largest_nesting_subsets (all_box_subsets)

  # print the largest number of boxes that fit

  # print the number of sets of such boxes

if __name__ == "__main__":
  main()

