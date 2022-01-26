#  File: Palindrome.py

#  Description: return the smallest palindrome given a user input word

#  Student Name: Zixi Lei

#  Student UT EID: zl7732

#  Partner Name: Wenxuan Jiang

#  Partner UT EID: wj3972

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 02/21/2021

#  Date Last Modified: 02/21/2021

import sys

# Input: a lowercase string with no digits, punctuation marks, or spaces
# Output: a string that is the smallest palindrome that can be 
#         made by adding characters to the start of the input string
def smallest_palindrome(str):
    # check is the number of digits we will compare forwards and backwords
    # strings with 2n+1 and 2n length will have the same check numb.
    check = len(str) // 2

    # this is the number of mismatches derived from the comparison of the first and last chr in the string
    error = 0

    # fix is the string with the chrs from the last error-digit places in the original string
    fix = ""
    output_string = ""

    # start checking the first and the end chr
    start = 0
    end = len(str) - 1

    # keep checking unless hitting check numb. and end index is greater than start (so the most extremecase
    # will be a adjacent comparison where start and end are in a left-right relation)
    while start <= check - 1 and end > start:
        # keep checking the next chr. start increases and end decreases
        if str[start] == str[end]:
            start += 1
            end -= 1

        # if they do not match, decrease the end index and record the numb. of mismatches in error
        else:
            error += 1
            end -= 1
            continue
            
    # If the string checks out to be a palindrome itself
    if start == check and error == 0:
        return str

    # return the smallest palindrom by adding the fix string, which is the reserve word of the last chrs. in original string
    else:
        # extract the fix word
        for i in range(1, error + 1):
            fix += str[-i]
        
        # add the fix string to the right of the original string to make a palindrome
        output_string = fix + str

        return output_string


# Input: no input
# Output: a string denoting all test cases have passed
def test_cases():
    # write your own test cases
    smallest_palindrome("a") == "a"
    smallest_palindrome("aa") == "aa"
    smallest_palindrome("madama") == "amadama"
    smallest_palindrome("cbabcde") == "edcbabcde"

    return "all test cases passed"

def main():
    # run your test cases
    '''
    print (test_cases())
    '''

    # read the data
    inFile = sys.stdin.read().strip().split("\n")

    # print the smallest palindromic string that can be made for each input
    for i in inFile:
        print(smallest_palindrome(i))

if __name__ == "__main__":
  main()