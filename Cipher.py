#  File: Cipher.py

#  Description: an algorithm to encrypt and decrypt given a string

#  Student Name: Zixi Lei

#  Student UT EID: zl7732

#  Partner Name: Wenxuan Jiang

#  Partner UT EID: wj3972

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 02/03/2021

#  Date Last Modified: 02/06/2021

import math
import sys

# Input: strng is a string of 100 or less of upper case, lower case,
#        and digits
# Output: function returns an encrypted string
def encrypt ( strng ):
    # Get the dimension and the number of asterisk of the matrix

    # Situation when the length of the strng is a perfect square
    if math.sqrt(len(strng)) - int(math.sqrt(len(strng))) == 0:
        dimension = int(math.sqrt(len(strng)))

    # When the length of the strng is NOT a perfect square
    else:
        dimension = int(math.sqrt(len(strng))) + 1
        numAsterisk = dimension ** 2 - len(strng)
        strng = strng + "*" * numAsterisk # Add asterisks

    # Put the string along with the asterisk(if any) into a matrix
    original_matrix = [[] for i in range(dimension)]
    orgin_text = list(strng)

    # Create a empty output encrypted matrix
    encrypted_matrix = [[] for i in range(dimension)]

    # Declare a index variable
    count = dimension - 1

    for i in range(dimension):
        for j in range(dimension):
            # Keep filling the 2D list with the characters in inputted string
            original_matrix[i].append(orgin_text[0])
            orgin_text.pop(0)

            # Fill out the output 2D list with letter A, which would be overrided later
            # This provides convenience to access the index later
            encrypted_matrix[i].append("A")

    for i in range(dimension):
        for j in range(dimension):
            # Encrypt the string and store them in encrypted_matrix
            encrypted_matrix[j][count] = original_matrix[i][j]
        count -= 1
    
    output_string = ""

    #convert the matrix back into the output string
    for i in range(len(encrypted_matrix)):
        for j in range(len(encrypted_matrix[i])):
            if encrypted_matrix[i][j] == "*":
                continue
            else:
                output_string += encrypted_matrix[i][j]

    return output_string


# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 
def decrypt ( strng ):
    # Get the dimension and the number of asterisk of the matrix

    # Situation when the length of the strng is a perfect square
    if math.sqrt(len(strng)) - int(math.sqrt(len(strng))) == 0:
        dimension = int(math.sqrt(len(strng)))

    # When the length of the strng is NOT a perfect square
    else:
        dimension = int(math.sqrt(len(strng))) + 1
        numAsterisk = dimension ** 2 - len(strng)
        strng = strng + "*" * numAsterisk # Add asterisks

    # Put everything into a matrix, which is used for decryption
    encrypted_matrix = [[] for i in range(dimension)]
    encrypted_text = list(strng)

    # Output matrix
    decrypted_matrix = [[] for i in range(dimension)]

    count = 0

    for i in range(dimension):
        for j in range(dimension):
            # Keep filling the 2D list with the characters in inputted string
            encrypted_matrix[i].append(encrypted_text[0])
            encrypted_text.pop(0)

            # Fill out the output 2D list with letter A, which would be overrided later
            # This provides convenience to access the index later
            decrypted_matrix[i].append("A")

    for i in range(dimension):
        for j in range(dimension):
            # decrypt the string and store them in decrypted_matrix
            decrypted_matrix[dimension - 1 - j][count] = encrypted_matrix[i][j]
        count += 1

    output_string = ""

    # convert the matrix into string
    for i in range(len(decrypted_matrix)):
        for j in range(len(decrypted_matrix[i])):
            if decrypted_matrix[i][j] == "*":
                continue
            else:
                output_string += decrypted_matrix[i][j]

    return output_string


def main():
  # read the two strings P and Q from standard input
  inputFile = sys.stdin.read().strip().split("\n")
  P = inputFile[0]
  Q = inputFile[1]

  # encrypt the string P
  encrypt(P)

  # decrypt the string Q
  decrypt(Q)

  # print the encrypted string of P and the
  print(encrypt(P))
  
  # decrypted string of Q to standard out
  print(decrypt(Q))

if __name__ == "__main__":
  main()