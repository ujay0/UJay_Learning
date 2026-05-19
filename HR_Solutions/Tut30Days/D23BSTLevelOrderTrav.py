# A level-order traversal, also known as a breadth-first search, 
# visits each level of a tree's nodes from left to right, top to 
# bottom. You are given a pointer,root , pointing to the root of a 
# binary search tree. Complete the levelOrder function provided 
# in your editor so that it prints the level-order traversal of
#  the binary search tree.



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

    def levelOrder(self,root):
        # Base case: if the tree is empty, return immediately
        if root is None:
            return
        
        # Initialize a queue to keep track of nodes to visit
        queue = []
        
        # Start with the root node in the queue
        queue.append(root)
        
        # Loop until there are no more nodes to visit
        while len(queue) > 0:
            # Dequeue the front node from the queue
            current_node = queue.pop(0)
            
            # Print the data of the current node followed by a space
            print(current_node.data, end=' ')
            
            # If the current node has a left child, enqueue it for later processing
            if current_node.left is not None:
                queue.append(current_node.left)
            
            # If the current node has a right child, enqueue it for later processing
            if current_node.right is not None:
                queue.append(current_node.right)


T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
