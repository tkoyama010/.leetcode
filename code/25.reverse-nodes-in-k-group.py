"""Module that contains a solution to the Reverse Nodes in k-Group problem."""


class Solution:
    """Provides a method to solve the Reverse Nodes in k-Group problem."""

    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:  # noqa: N802, F821
        """Reverse the nodes of a linked list in groups of k."""

        def reverse_list(
            head: ListNode | None,  # noqa: F821
            k: int,
        ) -> tuple[ListNode | None, ListNode | None, ListNode | None]:  # noqa: F821
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
