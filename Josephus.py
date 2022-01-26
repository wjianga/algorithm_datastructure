import sys

#  File: Josephus.py

#  Description: circularlist practice

#  Student Name: Zixi Lei

#  Student UT EID: zl7732

#  Partner Name: Wenxuan Jiang

#  Partner UT EID:wj3972

#  Course Name: CS 313E

#  Unique Number:52230

#  Date Created: 04/09/21

#  Date Last Modified: 04/11/21

class Link(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


class CircularList(object):
    # Constructor
    def __init__(self):
        self.first = None
        self.last = None
        


    # Insert an element (value) in the list
    def insert(self, data):
        new_link = Link(data)
        current = self.first

        # check if the circularlist is empty
        if (current == None):
            self.first = new_link
            self.last = new_link
            new_link.next = self.first
            return

        # if the circularlist is not empty, add the new_link to the end of the list
        else:
            while (current.next != self.first):
                current = current.next

        self.last.next = new_link
        self.last = new_link
        new_link.next = self.first



    # Find the Link with the given data (value)
    # or return None if the data is not there
    def find(self, data):
        current = self.first

        # if the list is none, directly return none
        if (current == None):
            return None

        # if the list is not none, check whether the current data is equal to the given data
        while (current.data != data):
            # if current.next equals to self.first, it means we already complete a circle
            if (current.next == self.first):
                return None
            else:
                current = current.next

        return current

    # Delete a Link with a given data (value) and return the Link
    # or return None if the data is not there
    def delete(self, data):
        previous = self.first
        current = self.first

        if (current == None):
            return None

        # while the data is not found
        while (current.data != data):
            # if proceeds to the last data but still not found, return non
            if (current.next == self.first):
                return None
            else:
                previous = current
                current = current.next

        # Found the data and the data is the head node
        if (current == self.first):
            if(self.first == self.last):
                self.first=None
                self.last=None
            else:
                self.first = self.first.next
                self.last.next = self.first
            # the data is at the end of the list
        elif(current == self.last):
            previous.next = self.first
            self.last = previous
        else:
            previous.next = current.next

        return current


    # Delete the nth Link starting from the Link start
    # Return the data of the deleted Link
    # AND return the next Link for the deleted Link
    def delete_after(self, start, n):
        current = start
        # for current in the range n-1
        for i in range(n-1):
            current = current.next
        # delete the current data
        self.delete(current.data)
        return (current.data, current.next)



    # Return a string representation of a Circular List
    # The format of the string will be the same as the __str__
    # format for normal Python lists
    def __str__(self):
        current = self.first
        string = ""
        # if the list is empty, return an empty bracket
        if (current == None):
            return '[]'
        # or add the element to the string
        else:
            string+='['
            while (current.next != self.first):
                string += str(current.data)+', '
                current = current.next
            # add the last data in the list
            string+=str(current.data)+']'

        return string




def main():
    # # read number of soldiers
    line = sys.stdin.readline()
    line = line.strip()
    num_soldiers = int(line)

    # # read the starting number
    line = sys.stdin.readline()
    line = line.strip()
    start_count = int(line)

    # # read the elimination number
    line = sys.stdin.readline()
    line = line.strip()
    elim_num = int(line)

    # # your code
    # create a new circularlist
    new_list = CircularList()
    # insert data in the list
    for i in range(num_soldiers):
        new_list.insert(i+1)
    # define the initial start link
    start_link = new_list.find(start_count)
    # while the list has more than 1 element
    while(new_list.first != new_list.last):
        result = new_list.delete_after(start_link,elim_num)
        start_link = result[1]
        print(result[0])
    # print the last data
    print(new_list.first.data)














if __name__ == "__main__":
    main()