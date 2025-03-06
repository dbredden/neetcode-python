# we are going to start off with two pointers prev & curr
# We will set prev to null & curr to head
# traverse through list until current = null
# store the next list node in a temp variable
# set the next pointer for current to the previous variable (this was previously just null)
# set previous to current
# set current to temp & return prev

""" class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next """

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev



