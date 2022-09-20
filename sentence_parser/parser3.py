# Implementation of a parser with grammar defined in the program and report error

# define the grammar
grammar = {
    'Sentence':     ('Noun-phrase', 'Verb-phrase'), # Rule 1
    'Noun-phrase':  ('Article', 'Noun'),            # Rule 2
    'Article':      ('a|an|the', None),             # Rule 3
    'Noun':         ('cat|rat', None),              # Rule 4
    'Verb-phrase':  ('Verb', 'Noun-phrase'),        # Rule 5
    'Verb':         ('ate|chased', None)            # Rule 6
}

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
    # get user input
    sentence = input('Enter a sentence: ').casefold().split()

    # prepare for parsing
    rule = 'Sentence'
    tree = ParseTreeNode(rule)
    marker = 0

    # parse and test for correctness
    if parse(tree, sentence):
        print('Sentence is grammatically correct.')
    else:
        print('Syntax error: "%s" is an invalid %s.' % (sentence[marker], rule))
