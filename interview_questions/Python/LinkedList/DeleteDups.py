from ..lib.linked_list import gen_linked_list_from_list, print_linked_list

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        slow_node = head
        fast_node = head
        while fast_node:
            if fast_node.val == slow_node.val:
                fast_node = fast_node.next
            else:
                slow_node.next = fast_node
                slow_node = fast_node

        # Fix the tail.
        if slow_node:
            slow_node.next = None
        return head

if __name__ == "__main__":
    l1 = gen_linked_list_from_list([1,1,2,3,3,4])
    head = Solution().deleteDuplicates(l1)
    print_linked_list(head)

    l1 = gen_linked_list_from_list([])
    head = Solution().deleteDuplicates(l1)
    print_linked_list(head)

    l1 = gen_linked_list_from_list([1])
    head = Solution().deleteDuplicates(l1)
    print_linked_list(head)

    l1 = gen_linked_list_from_list([1,1])
    head = Solution().deleteDuplicates(l1)
    print_linked_list(head)

    l1 = gen_linked_list_from_list([1,1,2])
    head = Solution().deleteDuplicates(l1)
    print_linked_list(head)

    l1 = gen_linked_list_from_list([1,2,2])
    head = Solution().deleteDuplicates(l1)
    print_linked_list(head)
