#  File: Reducible.py

#  Description: Implement hash table

#  Student Name: Zixi Lei

#  Student UT EID: zl7732

#  Partner Name: Wenxuan Jiang

#  Partner UT EID: wj3972

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 04/02/21

#  Date Last Modified: 04/03/2021

import sys

# Input: takes as input a positive integer n
# Output: returns True if n is prime and False otherwise
def is_prime ( n ):
    if (n == 1):
        return False

    limit = int (n ** 0.5) + 1
    div = 2
    while (div < limit):
        if (n % div == 0):
            return False
        div += 1
    return True

# Input: takes as input a string in lower case and the size
#        of the hash table
# Output: returns the index the string will hash into
def hash_word (s, size):
    hash_idx = 0
    for j in range (len(s)):
        letter = ord (s[j]) - 96
        hash_idx = (hash_idx * 26 + letter) % size
    return hash_idx

# Input: takes as input a string in lower case and the constant
#        for double hashing 
# Output: returns the step size for that string 
def step_size (s, const):
    return const - hash_word(s, const)

# Input: takes as input a string and a hash table 
# Output: no output; the function enters the string in the hash table, 
#         it resolves collisions by double hashing
def insert_word (s, hash_table):
    # mapped bucket index
    idx = hash_word(s, len(hash_table))

    # mapped bucket is empty, then insert the string there
    if hash_table[idx] == "":
        hash_table[idx] = s

    # step size
    # constant being 5
    step = step_size(s, 5)

    if hash_table[idx] == s:
        hash_table[idx] = s

    # collsion
    else:
        # if the bucket is not empty, keep looking for the next empty bucket
        while hash_table[idx] != "" and hash_table[idx] != s: #and idx != hash_word(s, len(hash_table)):
            idx = (idx + step) % len(hash_table)

        hash_table[idx] = s

# Input: takes as input a string and a hash table 
# Output: returns True if the string is in the hash table 
#         and False otherwise
def find_word (s, hash_table):
    # mapped bucket index
    idx = hash_word(s, len(hash_table))

    # if the string is at its mapped bucket
    if hash_table[idx] == s:
        return True

    # step size, with constant being 5
    step = step_size(s, 5)  
    idx1 = (idx + step) % len(hash_table)
    
    # if the string is not met and the loop is not completed, keep looking
    while idx1 != idx:
        # if the bucket is empty
        if hash_table[idx1] == "":
            return False

        if hash_table[idx1] == s:
            return True
        
        idx1 = (idx1 + step) % len(hash_table)
        
    return False


# Input: string s, a hash table, and a hash_memo 
#        recursively finds if the string is reducible
# Output: if the string is reducible it enters it into the hash memo 
#         and returns True and False otherwise
def is_reducible (s, hash_table, hash_memo):
    # base case
    # the letter is either a, i, o
    if len(s) == 1:
        return (s == "a" or s == "i" or s == "o")
    else:
        # check if the word is in hash memo
        if find_word(s, hash_memo):
            return True

        # check if the word is valid
        if not find_word(s, hash_table):
            return False

        # recursive case
        for i in range(len(s)):
            # if the substring is reducible, then this word is reducible
            if is_reducible(s[:i] + s[i + 1:], hash_table, hash_memo):
                insert_word(s, hash_memo)
                return True
        
        return False

# Input: string_list a list of words
# Output: returns a list of words that have the maximum length
def get_longest_words (string_list):
    max_length = 0
    max_list = []

    for i in string_list:
        # longer string found
        if len(i) > max_length:
            max_length = len(i)
            max_list.clear()
            max_list.append(i)
        # same length
        elif len(i) == max_length:
            max_list.append(i)

    return max_list

def main():
    # create an empty word_list
    word_list = []

    # read words from words.txt and append to word_list
    for line in sys.stdin.readlines():
        line = line.strip()
        word_list.append(line)

    # find length of word_list
    word_length = len(word_list)
    
    # determine prime number N that is greater than twice
    # the length of the word_list
    N = 2 * word_length
    while not is_prime(N):
        N += 1

    # create an empty hash_list
    hash_list = []

    # populate the hash_list with N blank strings
    for i in range(N):
        hash_list.append("")

    # hash each word in word_list into hash_list
    # for collisions use double hashing
    for word in word_list:
        insert_word(word, hash_list)

    # create an empty hash_memo of size M
    # we do not know a priori how many words will be reducible
    # let us assume it is 10 percent (fairly safe) of the words
    # then M is a prime number that is slightly greater than 
    # 0.2 * size of word_list
    hash_memo = []

    M = 0.2 * word_length
    while not is_prime(M):
        M += 1
    
    # populate the hash_memo with M blank strings
    for j in range(int(M)):
        hash_memo.append("")

    # create an empty list reducible_words
    reducible_words = []

    # for each word in the word_list recursively determine
    # if it is reducible, if it is, add it to reducible_words
    # as you recursively remove one letter at a time check
    # first if the sub-word exists in the hash_memo. if it does
    # then the word is reducible and you do not have to test
    # any further. add the word to the hash_memo.
    for word in word_list:
        if is_reducible(word, hash_list, hash_memo):
            reducible_words.append(word)

    # find the largest reducible words in reducible_words
    largest = get_longest_words(reducible_words)

    # print the reducible words in alphabetical order
    # one word per line
    for i in sorted(largest):
        print(i)


if __name__ == "__main__":
  main()