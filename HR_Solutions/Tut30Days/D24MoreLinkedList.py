# A Node class is provided for you in the editor. A Node object has an 
# integer data field, data , and a Node instance pointer, next , pointing to another
#  node (i.e.: the next node in a list).

# A removeDuplicates function is declared in your editor, which takes a head 
# pointer to the  node of a linked list as a parameter. Complete 
# removeDuplicates so that it deletes any duplicate nodes from the list 
# and returns the head of the updated list.

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 


class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        #Write your code here
        print('Removing duplicates from the linked list...')
        # Base case: if the linked list is empty (head is None), we simply return
        if head is None:
            return head
        current = head
        # We traverse the linked list using a while loop that continues until we 
        # reach the end of the list (current.next is None). Inside the loop, 
        # we compare the data of the current node with the data of the next node. 
        # If they are equal, it means we have found a duplicate. In this case, we 
        # update the next pointer of the current node to skip over the duplicate 
        # node (current.next = current.next.next). This effectively removes the 
        # duplicate node from the linked list. If the data of the current node 
        # and the next node are not equal, it means there is no duplicate at this 
        # position, and we simply move to the next node by updating current to 
        # current.next. By doing this for every node in the linked list, we ensure 
        # that all duplicates are removed, and we return the head of the updated 
        # linked list at the end.
        while current.next is not None:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                # If the current node's data is not equal to the next node's data, 
                # we simply move to the next node
                current = current.next
        return head


mylist= Solution()
T=int(input('Enter the number of elements in the linked list: '))
head=None
for i in range(T):
    data=int(input(f'Enter the data for element {i+1}: '))
    head=mylist.insert(head,data)    
head=mylist.removeDuplicates(head)
mylist.display(head); 