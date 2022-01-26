#  File: Geometry.py

#  Description: developing several classes that are fundamental in Solid Geometry - Point, Sphere, Cube, and Cylinder

#  Student Name: Zixi Lei

#  Student UT EID: zl7732

#  Partner Name: Wenxuan Jiang

#  Partner UT EID: wj3972

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 02/06/2021

#  Date Last Modified: 02/10/2021

import math

import sys

class Point (object):
  # constructor with default values
  def __init__ (self, x = 0, y = 0, z = 0):
      self.x = float(x)
      self.y = float(y)
      self.z = float(z)

  # create a string representation of a Point
  # returns a string of the form (x, y, z)
  def __str__ (self):
      return '(' + str(self.x) + ', ' + str(self.y) + ', ' +str(self.z)+ ')'

  # get distance to another Point object
  # other is a Point object
  # returns the distance as a floating point number
  def distance (self, other):
      # Use math.hypot() method to calculate sqrt(x^2 + y^2 + z^2)
      return math.hypot(self.x - other.x, self.y - other.y, self.z - other.z)

  # test for equality between two points
  # other is a Point object
  # returns a Boolean
  def __eq__ (self, other):
      # To see if the different between corresponding coordinates is less than our tolerance. If yes, we would say two points are equal
      tol = 1.0e-6
      return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol) and (abs(self.z - other.z)) < tol)

class Sphere (object):
  # constructor with default values
  def __init__ (self, x = 0, y = 0, z = 0, radius = 1):
    self.x = float(x)
    self.y = float(y)
    self.z = float(z)
    self.center = Point(x, y, z)
    self.radius = float(radius)

  # returns string representation of a Sphere of the form:
  # Center: (x, y, z), Radius: value
  def __str__ (self):
    return "Center: (" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + "), Radius: " + str(self.radius)

  # compute surface area of Sphere
  # returns a floating point number
  def area (self):
    return float(4 * math.pi * math.pow(self.radius, 2))

  # compute volume of a Sphere
  # returns a floating point number
  def volume (self):
    return float(4/3 * math.pi * math.pow(self.radius, 3))

  # determines if a Point is strictly inside the Sphere
  # p is Point object
  # returns a Boolean
  def is_inside_point (self, p):
    orgin = Point(self.x, self.y, self.z)
    return p.distance(orgin) < self.radius

  # determine if another Sphere is strictly inside this Sphere
  # other is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, other):
    origin = Point(self.x, self.y, self.z)
    other_sphere_center = Point(other.x, other.y, other.z)
    # If the distance from the centers of two spheres plus the radius is less than the self one, then the other sphere is contained
    return origin.distance(other_sphere_center) + other.radius < self.radius

  # determine if a Cube is strictly inside this Sphere
  # determine if the eight corners of the Cube are strictly
  # inside the Sphere
  # a_cube is a Cube object
  # returns a Boolean
  def is_inside_cube (self, a_cube):
    orgin = Point(self.x, self.y, self.z)
    # Create 8 Point objects for the cube object
    corner_1 = Point(a_cube.x + 1/2 * a_cube.side, a_cube.y + 1/2 * a_cube.side, a_cube.z + 1/2 * a_cube.side)
    corner_2 = Point(a_cube.x + 1/2 * a_cube.side, a_cube.y + 1/2 * a_cube.side, a_cube.z - 1/2 * a_cube.side)
    corner_3 = Point(a_cube.x + 1/2 * a_cube.side, a_cube.y - 1/2 * a_cube.side, a_cube.z - 1/2 * a_cube.side)
    corner_4 = Point(a_cube.x + 1/2 * a_cube.side, a_cube.y - 1/2 * a_cube.side, a_cube.z + 1/2 * a_cube.side)
    corner_5 = Point(a_cube.x - 1/2 * a_cube.side, a_cube.y - 1/2 * a_cube.side, a_cube.z - 1/2 * a_cube.side)
    corner_6 = Point(a_cube.x - 1/2 * a_cube.side, a_cube.y - 1/2 * a_cube.side, a_cube.z + 1/2 * a_cube.side)
    corner_7 = Point(a_cube.x - 1/2 * a_cube.side, a_cube.y + 1/2 * a_cube.side, a_cube.z - 1/2 * a_cube.side)
    corner_8 = Point(a_cube.x - 1/2 * a_cube.side, a_cube.y + 1/2 * a_cube.side, a_cube.z + 1/2 * a_cube.side)

    # If all 8 points' distances from the origin are smaller than the radius, then the cube is inside the sphere.
    return corner_1.distance(orgin) < self.radius and corner_2.distance(orgin) < self.radius\
           and corner_3.distance(orgin) < self.radius and corner_4.distance(orgin) < self.radius\
           and corner_5.distance(orgin) < self.radius and corner_6.distance(orgin) < self.radius\
           and corner_7.distance(orgin) < self.radius and corner_8.distance(orgin) < self.radius

  # determine if a Cylinder is strictly inside this Sphere
  # a_cyl is a Cylinder object
  # returns a Boolean
  def is_inside_cyl (self, a_cyl):
    orgin = Point(self.x, self.y, self.z)
    # Treat cylinder as a cube and generate 8 point objects
    corner_1 = Point(a_cyl.x + a_cyl.radius, a_cyl.y + a_cyl.radius, a_cyl.z + 1/2 * a_cyl.height)
    corner_2 = Point(a_cyl.x + a_cyl.radius, a_cyl.y + a_cyl.radius, a_cyl.z - 1/2 * a_cyl.height)
    corner_3 = Point(a_cyl.x + a_cyl.radius, a_cyl.y - a_cyl.radius, a_cyl.z + 1/2 * a_cyl.height)
    corner_4 = Point(a_cyl.x + a_cyl.radius, a_cyl.y - a_cyl.radius, a_cyl.z - 1/2 * a_cyl.height)
    corner_5 = Point(a_cyl.x - a_cyl.radius, a_cyl.y + a_cyl.radius, a_cyl.z + 1/2 * a_cyl.height)
    corner_6 = Point(a_cyl.x - a_cyl.radius, a_cyl.y + a_cyl.radius, a_cyl.z - 1/2 * a_cyl.height)
    corner_7 = Point(a_cyl.x - a_cyl.radius, a_cyl.y - a_cyl.radius, a_cyl.z + 1/2 * a_cyl.height)
    corner_8 = Point(a_cyl.x - a_cyl.radius, a_cyl.y - a_cyl.radius, a_cyl.z - 1/2 * a_cyl.height)

    # If all 8 points' distances from the origin are smaller than the radius, then the cube is inside the sphere.
    return corner_1.distance(orgin) < self.radius and corner_2.distance(orgin) < self.radius\
           and corner_3.distance(orgin) < self.radius and corner_4.distance(orgin) < self.radius\
           and corner_5.distance(orgin) < self.radius and corner_6.distance(orgin) < self.radius\
           and corner_7.distance(orgin) < self.radius and corner_8.distance(orgin) < self.radius

  # determine if another Sphere intersects this Sphere
  # other is a Sphere object
  # two spheres intersect if they are not strictly inside
  # or not strictly outside each other
  # returns a Boolean
  def is_outside_sphere (self, other):
    point_1 = Point(self.x, self.y, self.z)
    point_2 = Point(other.x, other.y, other.z)

    return point_1.distance(point_2) > self.radius + other.radius

  def does_intersect_sphere (self, other):
    # Intersecting if not inside or outside
    return not (self.is_outside_sphere(other) or self.is_inside_sphere(other))

  # determine if a Cube intersects this Sphere
  # the Cube and Sphere intersect if they are not
  # strictly inside or not strictly outside the other
  # a_cube is a Cube object
  # returns a Boolean
  def is_outside_cube (self, a_cube):
    orgin = Point(self.x, self.y, self.z)
    # Take the cube and generate 8 point objects
    corner_1 = Point(a_cube.x + 1/2 * a_cube.side, a_cube.y + 1/2 * a_cube.side, a_cube.z + 1/2 * a_cube.side)
    corner_2 = Point(a_cube.x + 1/2 * a_cube.side, a_cube.y + 1/2 * a_cube.side, a_cube.z - 1/2 * a_cube.side)
    corner_3 = Point(a_cube.x + 1/2 * a_cube.side, a_cube.y - 1/2 * a_cube.side, a_cube.z - 1/2 * a_cube.side)
    corner_4 = Point(a_cube.x + 1/2 * a_cube.side, a_cube.y - 1/2 * a_cube.side, a_cube.z + 1/2 * a_cube.side)
    corner_5 = Point(a_cube.x - 1/2 * a_cube.side, a_cube.y - 1/2 * a_cube.side, a_cube.z - 1/2 * a_cube.side)
    corner_6 = Point(a_cube.x - 1/2 * a_cube.side, a_cube.y - 1/2 * a_cube.side, a_cube.z + 1/2 * a_cube.side)
    corner_7 = Point(a_cube.x - 1/2 * a_cube.side, a_cube.y + 1/2 * a_cube.side, a_cube.z - 1/2 * a_cube.side)
    corner_8 = Point(a_cube.x - 1/2 * a_cube.side, a_cube.y + 1/2 * a_cube.side, a_cube.z + 1/2 * a_cube.side)

    # Test to see if all 8 points are outside the sphere
    return corner_1.distance(orgin) > self.radius and corner_2.distance(orgin) > self.radius\
           and corner_3.distance(orgin) > self.radius and corner_4.distance(orgin) > self.radius\
           and corner_5.distance(orgin) > self.radius and corner_6.distance(orgin) > self.radius\
           and corner_7.distance(orgin) > self.radius and corner_8.distance(orgin) > self.radius
  
  def does_intersect_cube (self, a_cube):
    # Intersecting if not inside or outside
    return not (self.is_outside_cube(a_cube) or self.is_inside_cube(a_cube))

  # return the largest Cube object that is circumscribed
  # by this Sphere
  # all eight corners of the Cube are on the Sphere
  # returns a Cube object
  def circumscribe_cube (self):
    largest_cube = Cube(self.x, self.y, self.z, (2 * self.radius) / math.sqrt(3))
    return largest_cube

class Cube (object):
  # Cube is defined by its center (which is a Point object)
  # and side. The faces of the Cube are parallel to x-y, y-z,
  # and x-z planes.
  def __init__ (self, x = 0, y = 0, z = 0, side = 1):
    self.x = float(x)
    self.y = float(y)
    self.z = float(z)
    self.center = Point(x,y,z)
    self.side = float(side)


  # string representation of a Cube of the form:
  # Center: (x, y, z), Side: value
  def __str__ (self):
    return 'Center: (' + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + "), Side: " + str(self.side)


  # compute the total surface area of Cube (all 6 sides)
  # returns a floating point number
  def area (self):
    return 6 * self.side ** 2


  # compute volume of a Cube
  # returns a floating point number
  def volume (self):
    return self.side ** 3

  # determines if a Point is strictly inside this Cube
  # p is a point object
  # returns a Boolean
  def is_inside_point (self, p):
    #determine the maximum and minimum values of the cube's coordinates
    max_x= self.x + self.side / 2
    max_y= self.y + self.side / 2
    max_z= self.z + self.side / 2
    min_x = self.x - self.side / 2
    min_y = self.y - self.side / 2
    min_z = self.z - self.side / 2
    return (min_x < p.x < max_x) and (min_y < p.y < max_y) and (min_z < p.z < max_z)


  # determine if a Sphere is strictly inside this Cube
  # a_sphere is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, a_sphere):
    distance_diff = a_sphere.radius+self.center.distance(a_sphere.center)
    return distance_diff < self.side/2


  # determine if another Cube is strictly inside this Cube
  # other is a Cube object
  # returns a Boolean
  def is_inside_cube (self, other):
    # determine the maximum and minumum values of coordinates of the two cubes
    max_x = self.center.x + self.side / 2
    max_y = self.center.y + self.side / 2
    max_z = self.center.z + self.side / 2
    min_x = self.center.x - self.side / 2
    min_y = self.center.y - self.side / 2
    min_z = self.center.z - self.side / 2

    max_x2 = other.center.x + other.side / 2
    max_y2 = other.center.y + other.side / 2
    max_z2 = other.center.z + other.side / 2
    min_x2 = other.center.x - other.side / 2
    min_y2 = other.center.y - other.side / 2
    min_z2 = other.center.z - other.side / 2

    return (max_x2<max_x) and (max_y2<max_y) and (max_z2<max_z) and (min_x2>min_x) and (min_y2>min_y) and (min_z2>min_z)


  # determine if a Cylinder is strictly inside this Cube
  # a_cyl is a Cylinder object
  # returns a Boolean
  def is_inside_cylinder (self, a_cyl):
    max_x2 = a_cyl.x + a_cyl.radius
    min_x2 = a_cyl.x - a_cyl.radius
    max_y2 = a_cyl.y + a_cyl.height/2
    min_y2 = a_cyl.y - a_cyl.height/2
    max_z2 = a_cyl.z + a_cyl.radius
    min_z2 = a_cyl.z - a_cyl.radius

    max_x = self.center.x + self.side / 2
    max_y = self.center.y + self.side / 2
    max_z = self.center.z + self.side / 2
    min_x = self.center.x - self.side / 2
    min_y = self.center.y - self.side / 2
    min_z = self.center.z - self.side / 2

    return (max_x2 < max_x) and (max_y2<max_y) and (max_z2<max_z) and (min_x2>min_x) and (min_y2>min_y) and (min_z2>min_z)


  #helper function that determine if another Cube is strictly outside this Cube
  def is_outside_cube(self,other): #(8 points)
    #  return the maximum and minimum values of the cubes' coordinates
    corner_1_other = Point(other.x + 1/2 * other.side, other.y + 1/2 * other.side, other.z + 1/2 * other.side)
    corner_2_other = Point(other.x + 1/2 * other.side, other.y + 1/2 * other.side, other.z - 1/2 * other.side)
    corner_3_other = Point(other.x + 1/2 * other.side, other.y - 1/2 * other.side, other.z - 1/2 * other.side)
    corner_4_other = Point(other.x + 1/2 * other.side, other.y - 1/2 * other.side, other.z + 1/2 * other.side)
    corner_5_other = Point(other.x - 1/2 * other.side, other.y - 1/2 * other.side, other.z - 1/2 * other.side)
    corner_6_other = Point(other.x - 1/2 * other.side, other.y - 1/2 * other.side, other.z + 1/2 * other.side)
    corner_7_other = Point(other.x - 1/2 * other.side, other.y + 1/2 * other.side, other.z - 1/2 * other.side)
    corner_8_other = Point(other.x - 1/2 * other.side, other.y + 1/2 * other.side, other.z + 1/2 * other.side)

    return not self.is_inside_point(corner_1_other) and not self.is_inside_point(corner_2_other) and not self.is_inside_point(corner_3_other)\
           and not self.is_inside_point(corner_4_other) and not self.is_inside_point(corner_5_other) and not self.is_inside_point(corner_6_other)\
           and not self.is_inside_point(corner_7_other) and not self.is_inside_point(corner_8_other)


  # determine if another Cube intersects this Cube
  # two Cube objects intersect if they are not strictly
  # inside and not strictly outside each other
  # other is a Cube object
  # returns a Boolean
  def does_intersect_cube (self, other):
    return not (self.is_inside_cube(other) or self.is_outside_cube(other))

  # determine the volume of intersection if this Cube
  # intersects with another Cube
  # other is a Cube object
  # returns a floating point number
  def intersection_volume (self, other):
    # return the maximum and minimum values of coordinates of the cube
    max_x = self.center.x + self.side / 2
    max_y = self.center.y + self.side / 2
    max_z = self.center.z + self.side / 2
    min_x = self.center.x - self.side / 2
    min_y = self.center.y - self.side / 2
    min_z = self.center.z - self.side / 2

    max_x2 = other.center.x + other.side / 2
    max_y2 = other.center.y + other.side / 2
    max_z2 = other.center.z + other.side / 2
    min_x2 = other.center.x - other.side / 2
    min_y2 = other.center.y - other.side / 2
    min_z2 = other.center.z - other.side / 2

    minx = min_x if min_x > min_x2 else min_x2
    miny = min_y if min_y > min_y2 else min_y2
    minz = min_z if min_z > min_z2 else min_z2
    maxx = max_x if max_x < max_x2 else max_x2
    maxy = max_y if max_y < max_y2 else max_y2
    maxz = max_z if max_z < max_z2 else max_z2

    if self.does_intersect_cube(other):
      return (maxx - minx)*(maxy - miny)*(maxz - minz)
    else:
      return 0

  # return the largest Sphere object that is inscribed
  # by this Cube
  # Sphere object is inside the Cube and the faces of the
  # Cube are tangential planes of the Sphere
  # returns a Sphere object
  def inscribe_sphere (self):
    return Sphere(self.x, self.y, self.z, 0.5 * self.side)

class Cylinder (object):
  # Cylinder is defined by its center (which is a Point object),
  # radius and height. The main axis of the Cylinder is along the
  # z-axis and height is measured along this axis
  def __init__ (self, x = 0, y = 0, z = 0, radius = 1, height = 1):
    self.x = float(x)
    self.y = float(y)
    self.z = float(z)
    self.center = Point(x, y, z)
    self.radius = float(radius)
    self.height = float(height)

  # returns a string representation of a Cylinder of the form:
  # Center: (x, y, z), Radius: value, Height: value
  def __str__ (self):
    return "Center: (" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + "), Radius: " + str(self.radius) + ", Height: " + str(self.height)

  # compute surface area of Cylinder
  # returns a floating point number
  def area (self):
    return float(2 * math.pi * math.pow(self.radius, 2) + 2 * math.pi * self.radius * self.height)

  # compute volume of a Cylinder
  # returns a floating point number
  def volume (self):
    return float(math.pi * math.pow(self.radius, 2) * self.height)

  # determine if a Point is strictly inside this Cylinder
  # p is a Point object
  # returns a Boolean
  def is_inside_point (self, p):
    max_z = self.z + 1/2 * self.height
    min_z = self.z - 1/2 * self.height
    cyl_point = Point(self.x, self.y, 0)
    p_point = Point(p.x, p.y, 0)
    return min_z < p.z < max_z and p_point.distance(cyl_point) < self.radius

  # determine if a Sphere is strictly inside this Cylinder
  # a_sphere is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, a_sphere):

    # return the 8 points of the sphere
    corner_1 = Point(a_sphere.x + a_sphere.radius, a_sphere.y + a_sphere.radius, a_sphere.z + 1/2 * a_sphere.radius)
    corner_2 = Point(a_sphere.x + a_sphere.radius, a_sphere.y + a_sphere.radius, a_sphere.z - 1/2 * a_sphere.radius)
    corner_3 = Point(a_sphere.x + a_sphere.radius, a_sphere.y - a_sphere.radius, a_sphere.z + 1/2 * a_sphere.radius)
    corner_4 = Point(a_sphere.x + a_sphere.radius, a_sphere.y - a_sphere.radius, a_sphere.z - 1/2 * a_sphere.radius)
    corner_5 = Point(a_sphere.x - a_sphere.radius, a_sphere.y + a_sphere.radius, a_sphere.z + 1/2 * a_sphere.radius)
    corner_6 = Point(a_sphere.x - a_sphere.radius, a_sphere.y + a_sphere.radius, a_sphere.z - 1/2 * a_sphere.radius)
    corner_7 = Point(a_sphere.x - a_sphere.radius, a_sphere.y - a_sphere.radius, a_sphere.z + 1/2 * a_sphere.radius)
    corner_8 = Point(a_sphere.x - a_sphere.radius, a_sphere.y - a_sphere.radius, a_sphere.z - 1/2 * a_sphere.radius)

    # return the maximum and minimum value of the cylinder
    max_x = self.x + self.radius
    min_x = self.x - self.radius
    max_y = self.y + self.radius
    min_y = self.y - self.radius
    max_z = self.z + 1/2 * self.height
    min_z = self.z - 1/2 * self.height

    # determine if the eight points of the sphere is inside the cylinder
    return min_x < corner_1.x < max_x and min_y < corner_1.y < max_y and min_z < corner_1.z < max_z\
           and min_x < corner_2.x < max_x and min_y < corner_2.y < max_y and min_z < corner_2.z < max_z\
           and min_x < corner_3.x < max_x and min_y < corner_3.y < max_y and min_z < corner_3.z < max_z\
           and min_x < corner_4.x < max_x and min_y < corner_4.y < max_y and min_z < corner_4.z < max_z\
           and min_x < corner_5.x < max_x and min_y < corner_5.y < max_y and min_z < corner_5.z < max_z\
           and min_x < corner_6.x < max_x and min_y < corner_6.y < max_y and min_z < corner_6.z < max_z\
           and min_x < corner_7.x < max_x and min_y < corner_7.y < max_y and min_z < corner_7.z < max_z\
           and min_x < corner_8.x < max_x and min_y < corner_8.y < max_y and min_z < corner_8.z < max_z

  # determine if a Cube is strictly inside this Cylinder
  # determine if all eight corners of the Cube are inside
  # the Cylinder
  # a_cube is a Cube object
  # returns a Boolean
  def is_inside_cube (self, a_cube):
    # returns the 8 points of the cube
    corner_1 = Point(a_cube.x + 1/2 * a_cube.side, a_cube.y + 1/2 * a_cube.side, a_cube.z + 1/2 * a_cube.side)
    corner_2 = Point(a_cube.x + 1/2 * a_cube.side, a_cube.y + 1/2 * a_cube.side, a_cube.z - 1/2 * a_cube.side)
    corner_3 = Point(a_cube.x + 1/2 * a_cube.side, a_cube.y - 1/2 * a_cube.side, a_cube.z - 1/2 * a_cube.side)
    corner_4 = Point(a_cube.x + 1/2 * a_cube.side, a_cube.y - 1/2 * a_cube.side, a_cube.z + 1/2 * a_cube.side)
    corner_5 = Point(a_cube.x - 1/2 * a_cube.side, a_cube.y - 1/2 * a_cube.side, a_cube.z - 1/2 * a_cube.side)
    corner_6 = Point(a_cube.x - 1/2 * a_cube.side, a_cube.y - 1/2 * a_cube.side, a_cube.z + 1/2 * a_cube.side)
    corner_7 = Point(a_cube.x - 1/2 * a_cube.side, a_cube.y + 1/2 * a_cube.side, a_cube.z - 1/2 * a_cube.side)
    corner_8 = Point(a_cube.x - 1/2 * a_cube.side, a_cube.y + 1/2 * a_cube.side, a_cube.z + 1/2 * a_cube.side)
    return self.is_inside_point(corner_1) and self.is_inside_point(corner_2) and self.is_inside_point(corner_3)\
           and self.is_inside_point(corner_4) and self.is_inside_point(corner_5) and self.is_inside_point(corner_6)\
           and self.is_inside_point(corner_7) and self.is_inside_point(corner_8)

  # determine if another Cylinder is strictly inside this Cylinder
  # other is Cylinder object
  # returns a Boolean
  def is_inside_cylinder (self, other):
    other_center = Point(other.x, other.y, other.z)
    center = Point(self.x, self.y, self.z)
    return other.radius < self.radius and other_center.distance(center) < math.hypot(self.radius, 1/2 * self.height) and other.height < self.height

  # determine if another Cylinder intersects this Cylinder
  # two Cylinder object intersect if they are not strictly
  # inside and not strictly outside each other
  # other is a Cylinder object
  # returns a Boolean
  def is_outside_cylinder (self, other): #(check radius in xy plane and range of z)
    # helper function that determines if a cylinder is outside another cyliner
    max_z_self = self.z + 1/2 * self.height
    min_z_self = self.z - 1/2 * self.height
    max_z = other.z + 1/2 * other.height
    min_z = other.z - 1/2 * other.height
    point_self = Point(self.x, self.y, 0)
    point_other = Point(other.x, other.y, 0)

    return min_z > max_z_self or min_z_self > max_z or max_z < min_z_self or max_z_self < max_z or point_self.distance(point_other) > self.radius + other.radius

  def does_intersect_cylinder (self, other):
    return not (self.is_inside_cylinder(other) or self.is_outside_cylinder(other))

def main():
  # read data from standard input
  inputFile = sys.stdin.read().split("\n")

  # read the coordinates of the first Point p
  point_1 = inputFile[0].split("#")[0].split()

  # create a Point object
  p = Point(float(point_1[0]), float(point_1[1]), float(point_1[2]))

  # read the coordinates of the second Point q
  point_2 = inputFile[1].split("#")[0].split()

  # create a Point object
  q = Point(float(point_2[0]), float(point_2[1]), float(point_2[2]))

  # read the coordinates of the center and radius of sphereA
  sphere_1 = inputFile[2].split("#")[0].split()

  # create a Sphere object
  sphereA = Sphere(float(sphere_1[0]), float(sphere_1[1]), float(sphere_1[2]), float(sphere_1[3]))

  # read the coordinates of the center and radius of sphereB
  sphere_2 = inputFile[3].split("#")[0].split()

  # create a Sphere object
  sphereB = Sphere(float(sphere_2[0]), float(sphere_2[1]), float(sphere_2[2]), float(sphere_2[3]))

  # read the coordinates of the center and side of cubeA
  cube_1 = inputFile[4].split("#")[0].split()

  # create a Cube object
  cubeA = Cube(float(cube_1[0]), float(cube_1[1]), float(cube_1[2]), float(cube_1[3]))

  # read the coordinates of the center and side of cubeB
  cube_2 = inputFile[5].split("#")[0].split()

  # create a Cube object
  cubeB = Cube(float(cube_2[0]), float(cube_2[1]), float(cube_2[2]), float(cube_2[3]))

  # read the coordinates of the center, radius and height of cylA
  cyl_1 = inputFile[6].split("#")[0].split()

  # create a Cylinder object
  cylA = Cylinder(float(cyl_1[0]), float(cyl_1[1]), float(cyl_1[2]), float(cyl_1[3]))

  # read the coordinates of the center, radius and height of cylB
  cyl_2 = inputFile[7].split("#")[0].split()
  
  # create a Cylinder object
  cylB = Cylinder(float(cyl_2[0]), float(cyl_2[1]), float(cyl_2[2]), float(cyl_2[3]))

  # print if the distance of p from the origin is greater than the distance of q from the origin
  origin = Point()
  if(p.distance(origin)>q.distance(origin)):
    print("Distance of Point p from the origin is greater than the distance of Point q from the origin")
  else:
    print("Distance of Point p from the origin is not greater than the distance of Point q from the origin")

  # print if Point p is inside sphereA
  if(sphereA.is_inside_point(p)):
    print("Point p is inside sphereA")
  else:
    print("Point p is not inside sphereA")


  # print if sphereB is inside sphereA
  if(sphereA.is_inside_sphere(sphereB)):
    print("sphereB is inside sphereA")
  else:
    print("sphereB is not inside sphereA")


  # print if cubeA is inside sphereA
  if(sphereA.is_inside_cube(cubeA)):
    print("cubeA is inside sphereA")
  else:
    print("cubeA is not inside sphereA")

  # print if cylA is inside sphereA
  if(sphereA.is_inside_cyl(cylA)):
    print("cylA is inside sphereA")
  else:
    print("cylA is not inside sphereA")

  # print if sphereA intersects with sphereB
  if(sphereA.does_intersect_sphere(sphereB)):
    print("sphereA does intersect sphereB")
  else:
    print("sphereA does not intersect sphereB")

  # print if cubeB intersects with sphereB
  if(sphereB.does_intersect_cube(cubeB)):
    print("cubeB does intersect sphereB")
  else:
    print("cubeB does not intersect sphereB")

  # print if the volume of the largest Cube that is circumscribed by sphereA is greater than the volume of cylA
  if (sphereA.circumscribe_cube().volume() > cylA.volume()):
    print("Volume of the largest Cube that is circumscribed by sphereA is greater than the volume of cylA")
  else:
    print("Volume of the largest Cube that is circumscribed by sphereA is not greater than the volume of cylA")

  # print if Point p is inside cubeA
  if (cubeA.is_inside_point(p)):
    print("Point p is inside cubeA")
  else:
    print("Point p is not inside cubeA")

  # print if sphereA is inside cubeA
  if(cubeA.is_inside_sphere(sphereA)):
    print("sphereA is inside cubeA")
  else:
    print("sphereA is not inside cubeA")


  # print if cubeB is inside cubeA
  if (cubeA.is_inside_cube(cubeB)):
    print("cubeB is inside cubeA")
  else:
    print("cubeB is not inside cubeA")

  # print if cylA is inside cubeA
  if (cubeA.is_inside_cylinder(cylA)):
    print("cylA is inside cubeA")
  else:
    print("cylA is not inside cubeA")

  # print if cubeA intersects with cubeB
  if(cubeA.does_intersect_cube(cubeB)):
    print("cubeA does intersect cubeB")
  else:
    print("cubeA does not intersect cubeB")

  # print if the intersection volume of cubeA and cubeB is greater than the volume of sphereA
  if (cubeA.intersection_volume(cubeB) > sphereA.volume()):
    print("Intersection volume of cubeA and cubeB is greater than the volume of sphereA")
  else:
    print("Intersection volume of cubeA and cubeB is not greater than the volume of sphereA")

  # print if the surface area of the largest Sphere object inscribed by cubeA is greater than the surface area of cylA
  if (cubeA.inscribe_sphere().area() > cylA.area()):
    print("Surface area of the largest Sphere object inscribed by cubeA is greater than the surface area of cylA")
  else:
    print("Surface area of the largest Sphere object inscribed by cubeA is not greater than the surface area of cylA")

  # print if Point p is inside cylA
  if (cylA.is_inside_point(p)):
    print("Point p is inside cylA")
  else:
    print("Point p is not inside cylA")

  # print if sphereA is inside cylA
  if (cylA.is_inside_sphere(sphereA)):
    print("sphereA is inside cylA")
  else:
    print("sphereA is not inside cylA")

  # print if cubeA is inside cylA
  if (cylA.is_inside_cube(cubeA)):
    print("cubeA is inside cylA")
  else:
    print("cubeA is not inside cylA")

  # print if cylB is inside cylA
  if (cylA.is_inside_cylinder(cylB)):
    print("cylB is inside cylA")
  else:
    print("cylB is not inside cylA")

  # print if cylB intersects with cylA
  if (cylA.does_intersect_cylinder(cylB)):
    print("cylB does intersect cylA")
  else:
    print("cylB does not intersect cylA")


if __name__ == "__main__":
  main()