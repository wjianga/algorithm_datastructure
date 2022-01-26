#  File: TestBinaryTree.py

#  Description: test a variety of binary tree methods

#  Student Name: Wenxuan Jiang

#  Student UT EID: wj3972

#  Partner Name: Zixi Lei

#  Partner UT EID: zl7732

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 04/26/2021

#  Date Last Modified: 04/26/2021

import sys

class Node (object):
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None
        self.parent = None

class Tree (object):
    def __init__(self):
        self.root = None

    # insert data into the tree
    def insert(self, data):
        new_node = Node(data)

        if (self.root == None):
            self.root = new_node
            return
        else:
            current = self.root
            parent = self.root
            while (current != None):
                parent = current
                if (data < current.data):
                    current = current.lchild
                else:
                    current = current.rchild
            if (data < parent.data):
                parent.lchild = new_node
            else:
                parent.rchild = new_node


    # search for a node with a given node
    def search(self, data):
        current = self.root
        while (current != None) and (current.data != data):
            if (data < current.data):
                current = current.lchild
            else:
                current = current.rchild
        
        return current

    # in order traversal - left, center, right
    def in_order(self, aNode):
        if(aNode != None):
            # visit the left subtree
            self.in_order(aNode.lchild)
            print(aNode.data)
            self.in_order(aNode.rchild)

    # find minimum in a tree
    def find_min(self):
        current = self.root
        
        if (current == None):
            return None

        while (current.lchild != None):
            current = current.lchild

        return current

    # recursion helper function for is_similar
    def is_similar_helper(self, c, other_c):
        if (c == None and other_c == None): # two trees are both None
            return True
        elif (c == None and other_c != None): # self tree is None
            return False
        elif (c != None and other_c == None): # the other tree is None
            return False
        # keep checking if the current node of both trees are the same
        elif (c.data == other_c.data):
            return (self.is_similar_helper(c.lchild, other_c.lchild)) \
                and (self.is_similar_helper(c.rchild, other_c.rchild))
        # otherwise
        else:
            return False

    # Returns true if two binary trees are similar
    def is_similar (self, pNode):
        return (self.is_similar_helper(self.root, pNode.root))

    # recursion helper function for get_level
    def get_level_helper(self, c_node, c_level, target_level):
        # if target level is met
        if (c_level == target_level):
            return [c_node]
        else:
            if (c_node.lchild != None and c_node.rchild != None): # the current node has both children
                return self.get_level_helper(c_node.lchild, c_level + 1, target_level) \
                + self.get_level_helper(c_node.rchild, c_level + 1, target_level)

            elif (c_node.lchild == None and c_node.rchild != None): # the node only has right child
                return self.get_level_helper(c_node.rchild, c_level + 1, target_level)

            elif (c_node.lchild != None and c_node.rchild == None): # the node only has left child
                return self.get_level_helper(c_node.lchild, c_level + 1, target_level)

            # out of reach
            else:
                return []

    # Returns a list of nodes at a given level from left to right
    def get_level (self, level):
        # empty tree
        if (self.root == None):
            return []
        else:
            return self.get_level_helper(self.root, 0, level)

    # recursion helper function for get_height
    def get_height_helper(self, c):
        if (c==None):
            return 0
        # divide and conquer
        else:
            height_left = self.get_height_helper(c.lchild)
            height_right = self.get_height_helper(c.rchild)
            return (max(height_left,height_right)) + 1

    # Returns the height of the tree
    def get_height (self):
        # empty tree
        if (self.root == None):
            return 0
        # only the root node
        elif (self.root.lchild== None and self.root.rchild == None):
            return 1
        else:
            return (self.get_height_helper(self.root))

    # recursion helper function for num_nodes
    def num_nodes_helper(self, c):
        if (c == None):
            return 0
        # divide and conquer
        else:
            count_left = self.num_nodes_helper(c.lchild)
            count_right= self.num_nodes_helper(c.rchild)
            return (count_left + count_right + 1)

    # Returns the number of nodes in the left subtree and
    # the number of nodes in the right subtree and the root
    def num_nodes (self):
        return (self.num_nodes_helper(self.root))


def main():
    #Create three trees - two are the same and the third is different
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree1_input = list (map (int, line)) 	# converts elements into ints


    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree2_input = list (map (int, line)) 	# converts elements into ints


    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree3_input = list (map (int, line)) 	# converts elements into ints

    # tree1 = Tree()
    # tree2 = Tree()

    # for i in range(len(tree1_input)):
    #     tree1.insert(tree1_input[i])

    # for j in range(len(tree2_input)):
    #     tree2.insert(tree2_input[j])

    # # Test your method is_similar()
    # tree1.is_similar(tree2)

    # Print the various levels of two of the trees that are different

    # Get the height of the two trees that are different

    # Get the total number of nodes a binary search tree

if __name__ == "__main__":
  main()
