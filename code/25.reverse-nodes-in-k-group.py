"""Module that contains a solution to the Reverse Nodes in k-Group problem."""

from __future__ import annotations

from typing import ListNode


class Solution:
    """Provides a method to solve the Reverse Nodes in k-Group problem."""

    def reverse_k_group(self: Solution, head: ListNode | None, k: int) -> ListNode | None:
        """Reverse the nodes of a linked list in groups of k."""

        def reverse_list(
            head: ListNode | None,
            k: int,
        ) -> tuple[ListNode | None, ListNode | None, ListNode | None]:
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
        tail.next = self.reverse_k_group(next_group_head, k)

        return new_head
