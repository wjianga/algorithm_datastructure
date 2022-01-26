#  File: Radix.py

#  Description: Radix sort on string with numbers and lower case characters

#  Student Name: Wenxuan Jiang

#  Student UT EID: wj3972

#  Partner Name: Zixi Lei

#  Partner UT EID: zl7732

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 04/07/2021

#  Date Last Modified: 04/07/2021

import sys

# Input: a is a list of strings that have either lower case
#        letters or digits
# Output: returns a sorted list of strings
def radix_sort (a):
    numb_zeros = {} # dict to record how many 0s padded to the right

    queues = [[] for i in range(37)] # 2d list representing queues
    
    max_pass = 0

    # extract the max length
    for i in a:
      if len(i) > max_pass:
        max_pass = len(i)

    # pad 0 to the right
    for i in range(len(a)):
      if len(a[i]) < max_pass:
        zeros = max_pass - len(a[i]) # numbers of zeros padded to the right
        a[i] = a[i] + (max_pass - len(a[i])) * "0" # new string created
        numb_zeros[a[i]] = zeros # record number of zeros to a dict
        queues[36].append(a[i])
      else:
        numb_zeros[a[i]] = 0
        queues[36].append(a[i])

    # perform this process max_pass times
    for i in range(max_pass):

      # enqueues using the [-i - 1]-th place chr
      for string in queues[36]:
        # numbers
        if 48 <= ord(string[-i - 1]) <= 57:
          queues[ord(string[-i - 1]) - 48].append(string)
        # lower case charater
        elif 97 <= ord(string[-i - 1]) <= 122:
          queues[ord(string[-i - 1]) - 87].append(string)

      queues[36].clear()
    
      # dequeues based on FIFO
      for m in range(len(queues) - 1):
        for n in range(len(queues[m])):
          queues[36].append(queues[m][n])
        
        queues[m].clear()

    for i in range(len(queues[36])):
      queues[36][i] = queues[36][i][:max_pass - numb_zeros[queues[36][i]]]

    return queues[36]

def main():
  # read the number of words in file
  line = sys.stdin.readline()
  line = line.strip()
  num_words = int (line)

  # create a word list
  word_list = []
  for i in range (num_words):
    line = sys.stdin.readline()
    word = line.strip()
    word_list.append (word)

  '''
  # print word_list
  print (word_list)
  '''

  # use radix sort to sort the word_list
  sorted_list = radix_sort (word_list)

  # print the sorted_list
  print (sorted_list)

if __name__ == "__main__":
  main()