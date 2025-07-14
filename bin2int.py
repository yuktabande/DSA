# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        num = ""
        ptr = head
        while ptr:
            num += str(ptr.val)
            ptr = ptr.next
        output = 0
        i = 0
        for j in reversed(num):
            j = int(j)
            output += j * (2**i)
            i += 1
        
        return output

        