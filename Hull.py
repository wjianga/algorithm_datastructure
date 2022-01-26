#  File: Hull.py

#  Description: create a convex hull that is the smallest convex polygon enclosing a set of points

#  Student Name: Zixi Lei

#  Student UT EID: zl7732

#  Partner Name: Wenxuan Jiang

#  Partner UT EID: wj3972

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 02/15/21

#  Date Last Modified: 02/17/21

import sys

import math

class Point (object):
  # constructor
  def __init__(self, x = 0, y = 0):
    self.x = x
    self.y = y

  # get the distance to another Point object
  def dist (self, other):
    return math.hypot (self.x - other.x, self.y - other.y)

  # string representation of a Point
  def __str__ (self):
    return '(' + str(self.x) + ', ' + str(self.y) + ')'

  # equality tests of two Points
  def __eq__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

  def __ne__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) >= tol) or (abs(self.y - other.y) >= tol))

  def __lt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y < other.y)
    return (self.x < other.x)

  def __le__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y <= other.y)
    return (self.x <= other.x)

  def __gt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y > other.y)
    return (self.x > other.x)

  def __ge__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y >= other.y)
    return (self.x >= other.x)

# Input: p, q, r are Point objects
# Output: compute the determinant and return the value
def det (p, q, r):
  # if the determinant returns a negative value, it means the third point is on the right side of the line
  # if the determinant returns a positive value, it means the third point is on the left side of the line
  # if the determinant returns zero, it means the three points are on the same line
  return (1 * (q.x * r.y - q.y * r.x)) - (p.x * (1 * r.y - 1 * q.y)) + (p.y * (1 * r.x - 1 * q.x))

# Input: sorted_points is a sorted list of Point objects
# Output: computes the convex hull of a sorted list of Point objects
#         convex hull is a list of Point objects starting at the
#         extreme left point and going clockwise in order
#         returns the convex hull
def convex_hull (sorted_points):
  #create two empty lists
  upper_hull = []
  lower_hull = []

  # the length of the sorted_points
  list_len = len(sorted_points)

  #append the first two points p_1 and p_2 in order into the upper_hull
  upper_hull.append(sorted_points[0])
  upper_hull.append(sorted_points[1])

  # append p_i from 3 to n
  for i in range (2, list_len):
    upper_hull.append(sorted_points[i])
    #while upper_hull contains three or more points and the last three points in upper_hull do not make a right turn
    #delete the middle of the last three points from upper_hull
    while(len(upper_hull) >= 3 and det(upper_hull[-3],upper_hull[-2],upper_hull[-1]) >= 0):
      upper_hull.pop(-2)

  #append the last two points p_n and p_n-1 in order into lower_hull with p_n as the first point.
  lower_hull.append(sorted_points[list_len-1])
  lower_hull.append(sorted_points[list_len-2])

  # append p_i from n-2 down to 1
  for i in range(list_len-3, -1, -1):
    lower_hull.append(sorted_points[i])
    #while lower_hull contains three or more points and the last three points in lower_hull do not make a right turn
    #delete the middle of the last three points from lower_hull
    while (len(lower_hull) >= 3 and det(lower_hull[-3], lower_hull[-2], lower_hull[-1]) >= 0):
      lower_hull.pop(-2)

  #remove the first and last points for lower_hull
  lower_hull.pop(0)
  lower_hull.pop(-1)

  #Append the points in the lower_hull to the points in the upper_hull and call those points the convex_hull
  convex_hull = []
  for i in range (len(lower_hull)):
    upper_hull.append(lower_hull[i])

  convex_hull = upper_hull

  return convex_hull


# Input: convex_poly is a list of Point objects that define the
#        vertices of a convex polygon in order
# Output: computes and returns the area of a convex polygon
def area_poly (convex_poly):
  # The first x coordinate would be the first x
  # The first y coordinate would be the second y
  x_index_plus = 0
  y_index_plus = 1

  det = 0

  # Keep adding up the multiples of the x and y till the index length - 1
  while x_index_plus <= len(convex_poly) - 2:
    det += convex_poly[x_index_plus].x * convex_poly[y_index_plus].y
    x_index_plus += 1
    y_index_plus += 1

  # Take care of the edge case where x index is at the end and y at the first 
  det = det + convex_poly[len(convex_poly) - 1].x * convex_poly[0].y

  # The first y coordinate would be the first y
  # The first x coordinate would be the second x
  y_index_minus = 0
  x_index_minus = 1

  # Take care of the edge case where y index is at the end and x at the first 
  while y_index_minus <= len(convex_poly) - 2:
    det -= convex_poly[y_index_minus].y * convex_poly[x_index_minus].x
    y_index_minus += 1
    x_index_minus += 1

  # Take care of the edge case where y index is at the end and x at the first 
  det = det - convex_poly[len(convex_poly) - 1].y * convex_poly[0].x

  # Compute the convex hull area
  area = (1 / 2) * abs(det)

  return area

# Input: no input
# Output: a string denoting all test cases have passed
def test_cases():
  # write your own test cases
  a = Point(0, 0)
  b = Point(0, 1)
  c = Point(1, 1)

  assert det(a, b, c) == -1

  return "all test cases passed"

def main():
  # create an empty list of Point objects
  points_list = []

  # read number of points
  line = sys.stdin.readline()
  line = line.strip()
  num_points = int (line)

  # read data from standard input
  for i in range (num_points):
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    x = int (line[0])
    y = int (line[1])
    points_list.append (Point (x, y))

  # sort the list according to x-coordinates
  sorted_points = sorted (points_list)


  # print the sorted list of Point objects
  #for p in sorted_points:
    #print (str(p))

  # get the convex hull
  convex_hull_result = convex_hull(sorted_points)

  # run your test cases
  """
  print(test_cases())
  """

  # print your results to standard output
  print("Convex Hull")
  # print the convex hull
  for p in convex_hull_result:
    print(str(p))

  # get the area of the convex hull
  area  = area_poly (convex_hull_result)


  # print the area of the convex hull
  print()
  print("Area of Convex Hull =",area)

if __name__ == "__main__":
  main()