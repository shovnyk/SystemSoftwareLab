# Simple depth first (post order) search of a tree

# Define a binary tree node
class BinaryTreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def dfs(self):
        # Traverse assuming current node to be the root of a binary tree
        if self.left != None:
            self.left.dfs()
        if self.right != None:
            self.right.dfs()
        print(self.val, end=" ")

    def dfs_leaf_only(self):
        # Print only the values of the leaf nodes
        if self.left != None:
            self.left.dfs_leaf_only()
        if self.right != None:
            self.right.dfs_leaf_only()

        if (self.left == None and self.right == None): # base case
            print(self.val, end=" ")

# Define a regular tree node
class TreeNode():
    def __init__(self, val, *children):
        self.val = val
        self.children = children

    def dfs(self):
        # Traverse taking current node as root
        for child in self.children:
            if child != None:
                child.dfs()
        print(self.val, end=" ")
        return 

if __name__ == '__main__':

    # Define a binary tree
    b = BinaryTreeNode("A",
            BinaryTreeNode("B", 
                    BinaryTreeNode("C"),
                    BinaryTreeNode("D")
                ), 
            BinaryTreeNode("E")
            )

    # Traverse it
    b.dfs()
    print()

    b.dfs_leaf_only()
    print()

    # Define a regular tree (with possibly more than 2 children per node)
    t = TreeNode("A",
            TreeNode("B", 
                TreeNode("E"),
                TreeNode("F")
            ),
            TreeNode("C",
                TreeNode("G"),
                TreeNode("H")
            ),
            TreeNode("D",
                TreeNode("I"),
                TreeNode("J"),
                TreeNode("K")
            )
        )

    # Traverse it
    t.dfs()
    print()
