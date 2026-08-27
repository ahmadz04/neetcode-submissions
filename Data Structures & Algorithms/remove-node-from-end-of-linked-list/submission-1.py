# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # Calculate the length of the linked list
        count = 0
        curr = head

        while curr:
            count += 1
            curr = curr.next

        # Operation: Abs of Length - n -> that's the index to be removed

        index_to_be_removed = abs(count - n)
        if index_to_be_removed == 0:
            return head.next

        # Traverse through the list and remove the node at index
        new_curr = head
        for i in range(count - 1):
            if(i + 1) == index_to_be_removed:
                new_curr.next = new_curr.next.next
                break
            new_curr = new_curr.next
        return head
        
