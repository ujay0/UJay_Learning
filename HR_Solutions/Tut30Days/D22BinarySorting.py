# The height of a binary search tree is the number of edges between 
# the tree's root and its furthest leaf. You are given a pointer, root, 
# pointing to the root of a binary search tree. Complete the getHeight 
# function provided in your editor so that it returns the height of the 
# binary search tree.


# The Node class is defined as follows:
class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        # Base case: if the node is None (leaf node's child or empty tree),
        # return -1 since there are no edges to count
        if root is None:
            return -1
        else:
            # Recursive call 1: Get the height of the left subtree
            # This recursively traverses down the left branch until it hits None,
            # then starts returning heights back up the call stack
            leftHeight = self.getHeight(root.left)
            
            # Recursive call 2: Get the height of the right subtree
            # This recursively traverses down the right branch until it hits None,
            # then starts returning heights back up the call stack
            rightHeight = self.getHeight(root.right)
            
            # Determine the maximum height between the two subtrees and add 1
            # The +1 represents the edge from the current node to its taller child
            # This builds up the final height as the recursion unwinds back to the root
            if leftHeight > rightHeight:
                return leftHeight + 1  # Left subtree is taller
            else:
                return rightHeight + 1  # Right subtree is taller or equal

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)       