# Implementation of a parser with grammar defined in the program (variation)

# define the grammar
grammar = {
    'S': ['NP', 'VP'],
    'NP': ['ART', 'N'], 
    'ART': ['a|an|the', None],
    'N': ['cat|rat', None],
    'VP': ['V', 'NP'],
    'V': ['ate|chased', None]
}

# define node for parse tree
class ParseTreeNode:
    def __init__(self, name, left=None, right=None):
        # each node of the parse tree
        self.name = name
        self.left = left
        self.right = right

    def leaves(self):
        # traverse the parse tree and print all leaf nodes
        if self.left != None:
            self.left.leaves()
        if self.right != None:
            self.right.leaves()
        
        if self.left == None and self.right == None and self.name != None:
            print(self.name, end=' ')

# generate parse tree based on sentence and defined grammar
def parse(tree, sentence):

    # use a global marker
    global marker 

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
    tree = ParseTreeNode('S')
    marker = 0

    # parse and test for correctness
    if parse(tree, sentence):
        print('Sentence is grammatically correct.')
    else:
        print('Sentence is grammatrically incorrect.')

    # print all the leaf nodes of parse tree
    tree.leaves()
    print()
