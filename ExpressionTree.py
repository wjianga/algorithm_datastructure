#  File: ExpressionTree.py

#  Description: evaluation of mathematical expression using binary seach tree and stack

#  Student Name: Wenxuan Jiang

#  Student UT EID: wj3972

#  Partner Name: Zixi Lei

#  Partner UT EID: zl7732

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 04/19/2021

#  Date Last Modified: 04/19/2021

import sys

operators = ['+', '-', '*', '/', '//', '%', '**']

class Stack (object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append (data)

    def pop(self):
        if(not self.is_empty()):
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

class Node (object):
    def __init__ (self, data = None, lChild = None, rChild = None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild

class Tree (object):
    def __init__ (self):
        self.root = None
    
    # this function takes in the input string expr and 
    # creates the expression tree
    def create_tree (self, expr):
        self.root = Node()

        # declare a stack and current node to root node
        stack = Stack()
        current = self.root

        # a list of tokens
        express = expr.split()

        # loop through each token in the list and
        # insert it into the binary search tree 
        for i in express:
            # token is left parenthesis
            if ( i == "(" ):
                current.lChild = Node()
                stack.push(current)
                current = current.lChild
            # token is operators
            elif (i in operators):
                current.data = i
                stack.push(current)
                current.rChild = Node()
                current = current.rChild
            # token is right parenthesis
            elif ( i == ")" ):
                if (not stack.is_empty()):
                    current = stack.pop()
            # token is operand
            else:
                current.data = i
                current = stack.pop()

    # this function should evaluate the tree's expression
    # returns the value of the expression after being calculated
    def evaluate (self, aNode):
        # if it is not at the leaves
        if(aNode.lChild != None and aNode.rChild != None):
           left = self.evaluate(aNode.lChild)
           right = self.evaluate(aNode.rChild)
        # if the current node is leaf nodes
        else:
            return float(aNode.data)

        # use eval() to evaluate the expression
        empty_str = ''
        empty_str += str(left)
        empty_str += str(aNode.data)
        empty_str += str(right)
        return eval(empty_str)


    # this function should generate the preorder notation of 
    # the tree's expression
    # returns a string of the expression written in preorder notation
    def pre_order (self, aNode):
        # if it is not at the leaves
        if (aNode.lChild != None and aNode.rChild != None):
            return str(aNode.data) + " " + str(self.pre_order(aNode.lChild)) + " " + str(self.pre_order(aNode.rChild))
        # if the current node is leaf nodes
        else:
            return str(aNode.data)

    # this function should generate the postorder notation of 
    # the tree's expression
    # returns a string of the expression written in postorder notation
    def post_order (self, aNode):
        # if it is not at the leaves
        if (aNode.lChild != None and aNode.rChild != None):
            return str(self.post_order(aNode.lChild)) + " " + str(self.post_order(aNode.rChild)) + " " + str(aNode.data)
        # if the current node is leaf nodes
        else:
            return str(aNode.data)

# you should NOT need to touch main, everything should be handled for you
def main():
    # read infix expression
    line = sys.stdin.readline()
    expr = line.strip()
 
    tree = Tree()
    tree.create_tree(expr)

    # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))

    # get the prefix version of the expression and print
    print("Prefix Expression:", tree.pre_order(tree.root).strip())

    # get the postfix version of the expression and print
    print("Postfix Expression:", tree.post_order(tree.root).strip())

if __name__ == "__main__":
    main()