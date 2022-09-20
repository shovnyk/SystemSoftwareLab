# Implementation of a parser with grammar defined in the program and report error

# from parser3 import grammar
import sys

# define node for parse tree
class ParseTreeNode:
    def __init__(self, name, left=None, right=None):
        # each node of the parse tree
        self.name = name
        self.left = left
        self.right = right

# generate parse tree based on sentence and defined grammar
def parse(tree, sentence):

    # modify global variables
    global marker, rule

    # basecase 0: if node is null
    if tree.name == None:
        return True

    # basecase 1: if word matches the node name
    if sentence[marker] in tree.name.split('|'): 
        tree.name = sentence[marker]
        marker = marker + 1 # move marker to next word
        return True

    # if not then check if rule is in grammar
    elif tree.name in grammar: 

        # expand tree at node
        rule = tree.name
        tree.left = ParseTreeNode(grammar[tree.name][0])
        tree.right = ParseTreeNode(grammar[tree.name][1])

        # search for words in left and right trees
        return parse(tree.left, sentence) and parse(tree.right, sentence)

    # word not in grammar
    else: return False

if __name__ == '__main__':
    # read grammar file and generate grammar
    grammarfile = open('grammar.txt')
    grammar = {}
    for line in grammarfile:
        line = line.split(':')
        rule = line[0]
        grammar[rule] = line[1].split()
        if len(grammar[rule]) < 2:
            grammar[rule].append(None)

    # read input file for sentences
    inputfile = open('input.txt')
    for line in inputfile:
        marker = 0
        rule = 'sentence'
        sentence = line.casefold().split()
        tree = ParseTreeNode(rule)
        print(line.rstrip(), end=':', flush=True)

        # parse sentences one by one for correctness
        if parse(tree, sentence):
            print("OK")
        else:
            print('Syntax error ("%s" is an invalid %s)' % (sentence[marker], rule),
                    file=sys.stderr)

    # # close files before exiting
    inputfile.close()
    grammarfile.close()
