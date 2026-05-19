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
        # Base case: If the current node (root) is None, we have found the correct
        # position to insert the new data. We create a new Node with the given data 
        # and return it to be linked to its parent node.
        if root==None:
            return Node(data)
        else:
            # Recursive case: If the current node is not None, we need to determine whether to insert the new data in the left subtree or the right subtree. 
            # We compare the new data with the current node's data. If the new data is less than or equal to the current
            # node's data, we will insert it into the left subtree. Otherwise, we will insert it into the right subtree.
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                # If the new data is greater than the current node's data, we will insert it into the right subtree. We make a recursive call to insert the new data into the right subtree and then link the returned node back to the current node's right pointer.
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