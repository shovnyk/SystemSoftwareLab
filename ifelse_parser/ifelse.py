# Implementation of a parser for parsing if else statements

import sys

# define the grammar for now
# later read it in from a file
grammar = {
        'ifelse': ['cond', 'act', 'else', 'act|ifelse'],
        'cond': ['var', 'boolop', 'var|const'],
        'act': ['asgn|pr'],
        'var': ['x|y|z'],
        'const': ['0|1|2|3|4|5|6|7|8|9'],
        'boolop': ['>|<|=='],
        'asgn': ['var', '<-', 'var|const'],
        'pr': ['print', 'var|const']
}

class ParseTreeNode:
    def __init__(self, name, children=None):
        # define the node of the tree
        self.name = name
        self.children = children

    def leaves(self):
        print(self.name, end=" ")
        if self.children == None:
            return
        for child in self.children:
            child.leaves()

# generate if else parse tree based on sentences and predefined grammar
def parse(tree, sentence):

    # glboal marker for keeping track of word in the input
    global marker

    # basecase 0:
    if sentence[marker] == 'if':
        marker = marker + 1
        tree.children = [ParseTreeNode(x) for x in grammar["ifelse"]]
        return all(parse(child, sentence) for child in tree.children)

    # basecase 1: if word matches the node name
    if sentence[marker] in tree.name.split('|'):
        tree.name = sentence[marker]
        marker = marker + 1
        return True
        
    # check if the rule exists in the grammar
    rules = tree.name.split('|')
    for rule in rules:
        if rule in grammar:
            # expand tree at the node
            tree.children = [ParseTreeNode(x) for x in grammar[rule]]

            # parse child trees and check if word can be found
            val = True
            for child in tree.children:
                val = val and parse(child, sentence)  # short circuit AND

            if val == True:
                tree.name = rule
                return True
            # else check alternate rule
    
    # word not in grammar
    return False

# read in a plain text file/user input and convert multiple words on possibly
# multiple lines into a single stream of text to be fed into the parser
def tokenize(openfile):
    sentence = []
    for line in openfile:
        sentence.extend(line.split())
    return sentence


# read in an input file and a grammar, tokenize it and the parse it to
# generate an if-else syntax tree, checking for syntax errors
if __name__ == '__main__':
    print("Enter a line of if-else code:")
    sentence = tokenize(sys.stdin)
    marker = 0
    tree = ParseTreeNode("ifelse");
    if parse(tree, sentence):
        print('Compiled Successfully')
    else:
        print(f'Compilation Error: at "{sentence[marker]}"')

    print("Syntax tree after parsing: ")
    tree.leaves()
    print()
