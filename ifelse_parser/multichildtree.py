# Implement a tree that has nodes with multiple children

class TreeNode:
    def __init__(self, name, children=None):
        self.name = name
        self.children = children

    def leaves(self):
        print(self.name, end=" ")
        if self.children == None:
            return
        for child in self.children:
            child.leaves()

t = TreeNode('hello', 
             [
                TreeNode('world', [TreeNode('a'), TreeNode('b')]), 
                TreeNode('foo', [TreeNode('x')]), 
                TreeNode('bar', [TreeNode('1'), TreeNode('2'), TreeNode('3')])
             ]
             );

t.leaves()
