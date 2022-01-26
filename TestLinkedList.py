#  File: TestLinkedList.py

#  Description: test linked list function

#  Student Name: Zixi Lei

#  Student UT EID: zl7732

#  Partner Name: Wenxuan Jiang

#  Partner UT EID:wj3972

#  Course Name: CS 313E

#  Unique Number:52230

#  Date Created: 04/05/21

#  Date Last Modified: 04/10/21

class Link(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


class LinkedList(object):
    # create a linked list
    # you may add other attributes
    def __init__(self):
        self.first = None

    # get number of links
    def get_num_links(self):
        # set a variable to record the number of links
        count = 0
        current = self.first
        # find the length of the linked list
        if (current == None):
            return 0
        else:
            while(current.next != None):
                count += 1
                current = current.next

            # return the length of the links
            return count + 1

    # add an item at the beginning of the list
    def insert_first(self, data):
        new_link = Link(data)
        new_link.next = self.first
        self.first = new_link

    # add an item at the end of a list
    def insert_last(self, data):
        new_link = Link(data)

        current = self.first

        # if the first links is none, add here
        if (current == None):
            self.first = new_link
            return

        # while the next link is not none, move on to the next node
        while (current.next != None):
            current = current.next

        current.next = new_link

    # add an item in an ordered list in ascending order
    # assume that the list is already sorted
    def insert_in_order(self, data):
        new_link = Link(data)
        current = self.first

        if (current == None):
            self.first = new_link
            return

        # while the next node is not none and smaller than the target data, move on to the next node
        while (current.next != None and current.next.data < new_link.data):
            current = current.next

        new_link.next = current.next
        current.next = new_link

    # search in an unordered list, return None if not found
    def find_unordered(self, data):
        current = self.first

        # if current node is none, return none
        if (current == None):
            return None

        # while current data is not the target data and the next node is not none,
        # move on to the next node
        while (current.data != data):
            if (current.next == None):
                return None
            else:
                current = current.next

        return current

    # Search in an ordered list, return None if not found
    def find_ordered(self, data):
        current = self.first

        if (current == None):
            return None

        # while current data smaller than the target data and the next node is not none,
        # move on to the next node
        while (current.data <= data):
            if (current.data == data):
                return current
                break
            elif (current.next == None):
                return None
            else:
                current = current.next

        return None

    # Delete and return the first occurrence of a Link containing data
    # from an unordered list or None if not found
    def delete_link(self, data):
        previous = self.first
        current = self.first

        if (current == None):
            return None

        while (current.data != data):
            if (current.next == None):
                return None
            else:
                previous = current
                current = current.next

        if (current == self.first):
            self.first = self.first.next
        else:
            previous.next = current.next

        return current


    # String representation of data 10 items to a line, 2 spaces between data
    def __str__(self):
        current = self.first
        string = ""
        if (current == None):
            return ''

        # set a variable to count the items
        count = 0

        # while the next node is not none, count plus one
        while(current.next!=None):
            count += 1

            # if it has 10 items one line, move on the a new line
            if (count% 10 == 0):
                string += str(current.data) + "\n"
            else:
                string+=str(current.data)+"  "
            current = current.next

        string += str(current.data)
        return string

    # Copy the contents of a list and return new list
    # do not change the original list
    def copy_list(self):
        current = self.first
        new_list = LinkedList()

        # if current is none, directly return the empty list
        if (current==None):
            return new_list
        # while the next node is not none, insert the data into the new_list
        else:
            while(current.next!=None):
                new_list.insert_last(current.data)
                current=current.next

            # insert the last element
            new_list.insert_last(current.data)
            return new_list


    # Reverse the contents of a list and return new list
    # do not change the original list
    def reverse_list(self):
        current = self.first
        new_list = LinkedList()

        # if current is none, directly return none
        if (current == None):
            return None

        # while next node is not none, insert the element in the reversed order
        while (current.next != None):
            new_list.insert_first(current.data)
            current = current.next

        # insert the last element of the original list at the beginning of the new list
        new_list.insert_first(current.data)
        return new_list


    # Sort the contents of a list in ascending order and return new list
    # do not change the original list
    def sort_list(self):
        current = self.first
        # create a new list and a new linked list
        new_list=[]
        new_linked_list=LinkedList()

        # if current is none, directly return none
        if (current == None):
            return None
        else:
            # while next node is not none, append the current data and move on to the next node
            while (current.next != None):
                new_list.append(current.data)
                current = current.next

        # append the last data and sort the list
        new_list.append(current.data)
        new_list = sorted(new_list)

        # insert the first link first
        new_linked_list.insert_first(new_list[0])

        # insert other links in order
        for i in range(1,len(new_list)):
            new_linked_list.insert_last(new_list[i])

        # return the sorted linked_list
        return new_linked_list


    # Return True if a list is sorted in ascending order or False otherwise
    def is_sorted(self):
        current = self.first

        if (current == None):
            return True

        # while the next node is not none
        while (current.next!=None):
            #  if the data is larger than the next data, return False since it is not sorted
            if (current.data > current.next.data):
                return False
            current = current.next

        return True


    # Return True if a list is empty or False otherwise
    def is_empty(self):
        # if the first element is none, it is empty
        return self.first is None


    # Merge two sorted lists and return new list in ascending order
    # do not change the original lists
    def merge_list(self, other):
        out = LinkedList()

        # define two first nodes
        current_a = self.first
        current_b = other.first

        # two lists are empty
        if (current_a == None and current_b ==None):
            return out
        
        # looping until both of them are empty
        while (current_a != None or current_b != None):
            # one of the list is empty
            if (current_a != None and current_b == None):
                out.insert_last(current_a.data)
                current_a = current_a.next
            # one of the list is empty
            elif (current_a == None and current_b !=None):
                out.insert_last(current_b.data)
                current_b = current_b.next
            # both of them are not empty
            else:
                # comparison
                if (current_a.data < current_b.data): # a is smaller
                    out.insert_last(current_a.data)
                    current_a = current_a.next
                elif (current_a.data > current_b.data): # b is smaller
                    out.insert_last(current_b.data)
                    current_b = current_b.next
                else: # they are equal to each other
                    out.insert_last(current_a.data)
                    current_a = current_a.next

        return out

    # Test if two lists are equal, item by item and return True
    def is_equal(self, other):
        # define two first nodes
        current_a = self.first
        current_b = other.first

        # if either of them is none, return False
        if (current_a == None or current_b ==None):
            return False
        # if both of them is none, return True
        elif (current_a == None and current_b ==None):
            return True
        # else if every link is the same, return True, otherwise False
        else:
            while (current_a.next != None and current_b.next != None):
              if (current_a.data != current_b.data):
                  return False
              current_a = current_a.next
              current_b = current_b.next

            # if the last nodes are not equal, return false
            if (current_a.data != current_b.data):
                return False

        return True

    # Return a new list, keeping only the first occurence of an element
    # and removing all duplicates. Do not change the order of the elements.
    # do not change the original list
    def remove_duplicates(self):
        out = LinkedList()
        seen = set()
        
        # set the first node
        current = self.first

        # looping till the end
        while (current != None):
            # already added, skip
            if (current.data in seen):
                current = current.next
            # add the element
            else:
                out.insert_last(current.data)
                seen.add(current.data)
        
        return out


def main():

    # Test methods insert_first() and __str__() by adding more than
    # 10 items to a list and printing it.
    test_list = LinkedList()

    test_list.insert_first(21)
    test_list.insert_first(20)
    test_list.insert_first(19)
    test_list.insert_first(18)
    test_list.insert_first(17)
    test_list.insert_first(16)
    test_list.insert_first(15)
    test_list.insert_first(14)
    test_list.insert_first(13)
    test_list.insert_first(12)


    test_list_2 = LinkedList()

    test_list_2.insert_first(2)
    test_list_2.insert_first(1)
    test_list_2.insert_first(3)
    test_list_2.insert_in_order(4)



    #print(test_list_2)
    #print(test_list_2.sort_list())
    #(test_list.merge_list(test_list_2))



    # Test method insert_last()

    # Test method insert_in_order()

    # Test method get_num_links()

    # Test method find_unordered()
    # Consider two cases - data is there, data is not there

    # Test method find_ordered()
    # Consider two cases - data is there, data is not there

    # Test method delete_link()
    # Consider two cases - data is there, data is not there

    # Test method copy_list()
    #print(test_list.copy_list())

    # Test method reverse_list()
    #print(test_list.reverse_list())

    # Test method sort_list()
    #print(test_list.sort_list())


    # Test method is_sorted()
    #print(test_list.is_sorted())


    # Consider two cases - list is sorted, list is not sorted

    # Test method is_empty()

    # Test method merge_list()

    # Test method is_equal()
    # Consider two cases - lists are equal, lists are not equal

    # Test remove_duplicates()

if __name__ == "__main__":
    main()