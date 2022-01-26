import sys


class Node(object):
    def __init__(self, data=None, lChild=None, rChild=None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild


class Tree(object):
    # the init() function creates the binary search tree with the
    # encryption string. If the encryption string contains any
    # character other than the characters 'a' through 'z' or the
    # space character drop that character.
    def __init__(self, encrypt_str):
        self.root = Node()

        for i in encrypt_str:
            if (97 <= ord(i) <= 122 or i == " "):
                self.insert(i)

    # the insert() function adds a node containing a character in
    # the binary search tree. If the character already exists, it
    # does not add that character. There are no duplicate characters
    # in the binary search tree.
    def insert(self, ch):
        current = self.root

        if (self.root.data == None):
            self.root.data = ch
            return

        # if (ch == " "):
        #     while (current.lChild != None):
        #         current = current.lChild
        #
        #     current.lChild = Node(ch)
        #     return
        parent = None

        while(current!=None):
            if(ch > current.data):
                parent = current
                current = current.rChild
            elif(ch < current.data):
                parent = current
                current = current.lChild
            else:
                return


        if (ch > parent.data):
            parent.rChild = Node(ch)
            return
        else:
            parent.lChild = Node(ch)
            return

    # the search() function will search for a character in the binary
    # search tree and return a string containing a series of lefts
    # (<) and rights (>) needed to reach that character. It will
    # return a blank string if the character does not exist in the tree.
    # It will return * if the character is the root of the tree.
    def search(self, ch):
        current = self.root

        path = ""

        if (self.root == None):
            return ""
        elif (ch == self.root.data):
            return "*"

        while (current != None):
            if (ch > current.data):
                path += ">"
                current = current.rChild
            elif (ch < current.data):
                path += "<"
                current = current.lChild
            else:
                return path

        return ""



    # the traverse() function will take string composed of a series of
    # lefts (<) and rights (>) and return the corresponding
    # character in the binary search tree. It will return an empty string
    # if the input parameter does not lead to a valid character in the tree.
    def traverse(self, st):
        current = self.root

        if (self.root == None):
            return ""
        elif (st == "*"):
            return str(self.root.data)

        for i in st:
            if (i == "<"):
                if (current.lChild == None):
                    return ""
                else:
                    current = current.lChild
            elif (i == ">"):
                if (current.rChild == None):
                    return ""
                else:
                    current = current.rChild
            else:
                continue

        return str(current.data)

    # the encrypt() function will take a string as input parameter, convert
    # it to lower case, and return the encrypted string. It will ignore
    # all digits, punctuation marks, and special characters.
    def encrypt(self, st):
        st = st.lower()

        path = ""

        for i in st:
            if (97 <= ord(i) <= 122 or i == " "):
                path += self.search(str(i)) + "!"

        return path[:-1]

    # the decrypt() function will take a string as input parameter, and
    # return the decrypted string.
    def decrypt(self, st):
        out = ""
        st = st.split("!")
        for i in st:
            out += self.traverse(str(i))
        return out


def main():
    # read encrypt string
    line = sys.stdin.readline()
    encrypt_str = line.strip()

    # create a Tree object
    the_tree = Tree(encrypt_str)

    # read string to be encrypted
    line = sys.stdin.readline()
    str_to_encode = line.strip()

    # print the encryption
    print(the_tree.encrypt(str_to_encode))

    # read the string to be decrypted
    line = sys.stdin.readline()
    str_to_decode = line.strip()

    # print the decryption
    print(the_tree.decrypt(str_to_decode))


if __name__ == "__main__":
    main()