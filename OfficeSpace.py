#  File: OfficeSpace.py

#  Description: a series of functions that represent requesting cubicles scenarios

#  Student Name: Wenxuan Jiang

#  Student UT EID: wj3972

#  Partner Name: Zixi Lei

#  Partner UT EID: zl7732

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 02/13/2021

#  Date Last Modified: 02/14/2021

import sys

# Input: a rectangle which is a tuple of 4 integers (x1, y1, x2, y2)
# Output: an integer giving the area of the rectangle
def area (rect):
    # Extract the width and height of the rectangle and take the multiple of them
    return int(abs(int(rect[2]) - int(rect[0])) * abs(int(rect[3]) - int(rect[1])))


# Input: two rectangles in the form of tuples of 4 integers
# Output: a tuple of 4 integers denoting the overlapping rectangle.
#         return (0, 0, 0, 0) if there is no overlap
def overlap (rect1, rect2):
    # X - From the right
    if rect1[0] <= rect2[0] < rect1[2]:
        # X - X1 and X2 bounded
        if rect1[0] < rect2[2]  <= rect1[2]:
            # Y - Y1 and Y2 out of range
            if rect2[1] < rect1[1] and rect2[3] > rect1[3]:
                return (rect2[0], rect1[1], rect2[2], rect1[3])
            # Y - Y1 bounded and Y2 out out of range
            elif rect1[1] <= rect2[1] < rect1[3] and rect2[3] >= rect1[3]:
                return (rect2[0], rect2[1], rect2[2], rect1[3])
            # Y - Y2 bounded and Y1 out out of range
            elif rect1[1] < rect2[3] <= rect1[3] and rect2[1] <= rect1[1]:
                return (rect1[0], rect2[1], rect2[2], rect2[3])
            # Y - Y1 and Y2 bounded
            elif rect1[1] < rect2[3] < rect1[3] and rect1[1] < rect2[1] < rect1[3]:
                return (rect2[0], rect2[1], rect2[2], rect2[3])
            else:
                return (0, 0, 0, 0)
        # X - X1 bounded and X2 out of range
        elif rect1[2] <= rect2[2]:
            # Y - Y1 and Y2 out of range
            if rect2[1] < rect1[1] and rect2[3] > rect1[3]:
                return (rect1[0], rect2[1], rect1[2], rect1[3])
            # Y - Y1 bounded and Y2 out out of range
            elif rect1[1] <= rect2[1] < rect1[3] and rect2[3] >= rect1[3]:
                return (rect2[0], rect2[1], rect1[2], rect1[3])
            # Y - Y2 bounded and Y1 out out of range
            elif rect1[1] < rect2[3] <= rect1[3] and rect2[1] <= rect1[1]:
                return (rect2[0], rect1[1], rect1[2], rect2[3])
            # Y - Y1 and Y2 bounded
            elif rect1[1] < rect2[3] < rect1[3] and rect1[1] < rect2[1] < rect1[3]:
                return (rect2[0], rect2[1], rect1[2], rect2[3])
            else:
                return (0, 0, 0, 0)

    # X - From the left
    if rect1[0] <= rect2[2] <= rect1[2]:
        # X-completely included
        if rect1[0] <= rect2[0] <= rect1[2]:
            # Y- y1, y2 out of range
            if rect2[3] > rect1[3] and rect2[1] < rect1[1]:
                return(rect2[0], rect1[1], rect2[2], rect1[3])
            # Y- y1 bounded and y2 out of range
            elif rect2[3] >= rect1[3] and rect1[1] <= rect2[1] < rect2[3]:
                return(rect2[0],rect2[1],rect2[2],rect1[3])
            # Y- y2 bounded and y1 out of range
            elif rect1[1] < rect2[3] <= rect1[3] and rect2[1]<=rect1[1]:
                return(rect2[0],rect1[1],rect2[2],rect2[3])
            # Y - y1, y2 bounded
            elif rect1[1]<=rect2[3]<=rect1[3] and rect1[1]<=rect2[1]<=rect1[3]:
                return (rect2[0],rect2[1],rect2[2],rect2[3])
            else:
                return (0, 0, 0, 0)

        # x2 bounded, x1 out of range
        elif rect1[0]>=rect2[0]:
            # Y- y1, y2 out of range
            if rect2[3] > rect1[3] and rect2[1] < rect1[1]:
                return (rect1[0], rect1[1], rect2[2], rect1[3])
            # Y- y1 bounded and y2 out of range
            elif rect2[3] >= rect1[3] and rect1[1] <= rect2[1] < rect2[3]:
                return (rect1[0], rect2[1], rect2[2], rect1[3])
            # Y- y2 bounded and y1 out of range
            elif rect1[1] < rect2[3] <= rect1[3] and rect2[1] <= rect1[1]:
                return (rect1[0], rect1[1], rect2[2], rect2[3])
            # Y - y1, y2 bounded
            elif rect1[1] <= rect2[3] <= rect1[3] and rect1[1] <= rect2[1] <= rect1[3]:
                return (rect2[0], rect2[1], rect2[2], rect2[3])
            else:
                return (0, 0, 0, 0)


# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the unallocated 
#         space in the office
def unallocated_space (bldg):
    count = 0
    
    # Loop through the 2D list
    # If the value of the entry in the 2D list is 0, then it means unallocated_space
    for i in range(len(bldg)):
        for j in range(len(bldg[i])):
            if bldg[i][j] == 0:
                count += 1

    return count


# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the contested 
#         space in the office
def contested_space (bldg):
    count = 0
    
    # Loop through the 2D list
    # If the value of the entry in the 2D list is greater than 1, then it means contested_space
    for i in range(len(bldg)):
        for j in range(len(bldg[i])):
            if bldg[i][j] > 1:
                count += 1

    return count


# Input: bldg is a 2-D array representing the whole office space
#        rect is a rectangle in the form of a tuple of 4 integers
#        representing the cubicle requested by an employee
# Output: a single integer denoting the area of the uncontested 
#         space in the office that the employee gets
def uncontested_space (bldg, rect):
    total_space = (rect[3]-rect[1]) * (rect[2]-rect[0])
    count = 0

    # loop through each employee's cubicles areas to find out if there are contested spaces
    for i in range(len(bldg)-rect[3],len(bldg)-rect[1]):
        for j in range(rect[0],rect[2]):
            if bldg[i][j] > 1:
                count += 1

    # return total space minus the area of conntested space
    return total_space - count


# Input: office is a rectangle in the form of a tuple of 4 integers
#        representing the whole office space
#        cubicles is a list of tuples of 4 integers representing all
#        the requested cubicles
# Output: a 2-D list of integers representing the office building and
#         showing how many employees want each cell in the 2-D list
def request_space (office, cubicles):
    # Create an empty 2D list with y2 - y1 height and x2 - x1 width
    office_list = [[0] * abs(int(office[2]) - int(office[0])) for i in range(abs(int(office[3]) - int(office[1])))]

    # Index the 2D list using the difference of the length of the list and the coordinates of cubicles requested by employees
    for i in range(len(cubicles)):
        for row in range(len(office_list) - cubicles[i][3], len(office_list) - cubicles[i][1]):
            for col in range(cubicles[i][0], cubicles[i][2]):
                office_list[row][col] += 1
    
    return office_list

# Input: no input
# Output: a string denoting all test cases have passed
def test_cases ():
    assert area ((0, 0, 1, 1)) == 1
    # write your own test cases
    assert request_space ((0, 0, 5, 5), [(0, 0, 2, 2), (1, 1, 3, 3)]) == [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 1, 1, 0, 0], [1, 2, 1, 0, 0], [1, 1, 0, 0, 0]]

    return "all test cases passed"

def main():
    # read the data
    inputFile = sys.stdin.read().split("\n")

    # run your test cases
    '''
    print (test_cases())
    '''

    # Put the office space into a tuple
    whole_office = (0, 0, inputFile[0].split()[0], inputFile[0].split()[1])

    # Create a tuple list regarding the cubicles requested by each employees
    list_of_tuples = []
    index = 2
    for i in range(int(inputFile[1])):
        list_of_tuples.append((int(inputFile[index].split()[1]), int(inputFile[index].split()[2]), int(inputFile[index].split()[3]), int(inputFile[index].split()[4])))
        index += 1

    list_after_fill = request_space (whole_office, list_of_tuples)

    # print the following results after computation

    # compute the total office space
    print("Total", area(whole_office))

    # compute the total unallocated space
    print("Unallocated", unallocated_space (list_after_fill))

    # compute the total contested space
    print("Contested", contested_space (list_after_fill))

    # compute the uncontested space that each employee gets
    for i in range(int(inputFile[1])):
        print(inputFile[2+i].split()[0],uncontested_space(list_after_fill, list_of_tuples[i]))

if __name__ == "__main__":
    main()