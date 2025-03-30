# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse_list(head, k):
            curr = head
            prev = None
            next_node = None
            count = 0

            while curr is not None and count < k:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
                count += 1

            return prev, head, next_node

        if not head:
            return None

        curr = head
        count = 0
        while curr and count < k:
            curr = curr.next
            count += 1

        if count < k:
            return head

        new_head, tail, next_group_head = reverse_list(head, k)
        tail.next = self.reverseKGroup(next_group_head, k)

        return new_head
