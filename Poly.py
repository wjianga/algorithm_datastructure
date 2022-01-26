import sys

class Link (object):
  def __init__ (self, coeff = 1, exp = 1, next = None):
    self.coeff = coeff
    self.exp = exp
    self.next = next

  def __str__ (self):
    return '(' + str (self.coeff) + ', ' + str (self.exp) + ')'

class LinkedList (object):
  def __init__ (self):
    self.first = None

  # keep Links in descending order of exponents
  def insert_in_order (self, coeff, exp):
    # link to insert
    new_link = Link(coeff, exp)

    # link in LinkedList to compare
    current = self.first

    # if the list is empty
    if (self.first == None):
      self.first = new_link
      return

    # if there is only one element in the list
    if (self.first.next == None):
      if (self.first.exp < new_link.exp):
        new_link.next = self.first
        self.first = new_link
        return
      elif (self.first.exp > new_link.exp):
        self.first.next = new_link
        return
      else:
        self.first.coeff += new_link.coeff
        return

    # while the next node is not none and the link to insert is smaller than next two terms
    while (current.next != None):
      # the polynimial to be inserted is greater than the first term
      if (self.first.exp < new_link.exp):
        new_link.next = self.first
        self.first = new_link
        return
      elif (current.exp == new_link.exp):
        current.coeff += new_link.coeff
        return
      # if the current term is greater than or equal to the link to be inserted
      # and the current.next is smaller than or equal to the link to be inserted, then insert
      elif (current.exp > new_link.exp and current.next.exp < new_link.exp):
        new_link.next = current.next
        current.next = new_link
        return
      # if next two terms are greater than the link to be inserted
      elif (current.exp > new_link.exp and current.next.exp > new_link.exp):
        current = current.next
        continue
      else:
        current = current.next
        continue

    # reach the end
    if (current.exp > new_link.exp):
      new_link.next = current.next
      current.next = new_link
    elif (current.exp == new_link.exp):
      current.coeff += new_link.coeff
      return


  # add polynomial p to this polynomial and return the sum
  def add (self, p):
    current = self.first
    pterm = p.first

    # first check if any of the polynomials is empty
    if (current == None and pterm == None):
      return self
    elif (current == None and pterm != None):
      return p
    elif (current != None and pterm == None):
      return self

    while (current != None and pterm!=None):
        if (current.exp == pterm.exp):
          current.coeff += pterm.coeff
          current = current.next
          pterm = pterm.next
        else:
          current = current.next

    # no term in self has same exponent as pterm has
    while (pterm != None):
     self.insert_in_order(pterm.coeff, pterm.exp)
     pterm = pterm.next

    return self

  # multiply polynomial p to this polynomial and return the product
  def mult (self, p):
    out = LinkedList()

    current = self.first
    pterm = p.first

    # first check if any of the polynomials is empty
    if (current == None and pterm == None):
      return self
    elif (current == None and pterm != None):
      return 0
    elif (current != None and pterm == None):
      return 0

    while (current != None):
      #while (pterm != None):
      if (pterm == None):
        current = current.next
        pterm = p.first
        if (current == None):
          return out

      out.insert_in_order((current.coeff * pterm.coeff), (current.exp + pterm.exp))
      pterm = pterm.next

    return out


  # create a string representation of the polynomial
  def __str__ (self):
    out = ""

    current = self.first

    if (current == None):
      return "()"

    while (current != None):
      if (current.coeff == 0):
        current = current.next
        continue
      elif len(out) == 0:
        out = out + "(" + str(current.coeff) + ", " + str(current.exp) + ")"
      else:
        out = out + " + " + "(" + str(current.coeff) + ", " + str(current.exp) + ")"

      current = current.next

    return out

def main():
  # read data from file poly.in from stdin
  infile = sys.stdin.read()
  list = infile.strip().split()

  # create polynomial p
  p = LinkedList()
  p1 = LinkedList()

  numb_pair1 = int(list[0])

  poly1 = list[1 : 2 * numb_pair1 + 1]

  for i in range(0, len(poly1), 2):
    p.insert_in_order(int(poly1[i]), int(poly1[i + 1]))
    p1.insert_in_order(int(poly1[i]), int(poly1[i + 1]))

  # create polynomial q
  q = LinkedList()

  numb_pair2 = list[2 * numb_pair1 + 1]

  poly2 = list[2 * numb_pair1 + 2 :]

  for i in range(0, len(poly2), 2):
    q.insert_in_order(int(poly2[i]), int(poly2[i + 1]))

  # get sum of p and q and print sum
  print(p.add(q))

  # get product of p and q and print product
  print(p1.mult(q))

if __name__ == "__main__":
  main()
