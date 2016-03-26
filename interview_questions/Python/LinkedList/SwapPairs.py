from ..lib.linked_list import gen_linked_list_from_list, print_linked_list, ListNode

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_head = ListNode(None)
        new_tail = new_head

        while head:
            node1 = head
            node2 = head.next
            if node2:
                tmp = head.next.next
                new_tail.next = node2
                new_tail = new_tail.next
                new_tail.next = None
            else:
                tmp = head.next

            new_tail.next = head
            new_tail = new_tail.next
            new_tail.next = None

            # print '%s %s' % (head.val, head.next.val)

            head = tmp

        return new_head.next


if __name__ == "__main__":
    head = gen_linked_list_from_list([])
    head = Solution().swapPairs(head)
    print_linked_list(head)

    head = gen_linked_list_from_list([1])
    head = Solution().swapPairs(head)
    print_linked_list(head)

    head = gen_linked_list_from_list([2,1])
    head = Solution().swapPairs(head)
    print_linked_list(head)

    head = gen_linked_list_from_list([1,2,3])
    head = Solution().swapPairs(head)
    print_linked_list(head)

    head = gen_linked_list_from_list([1,2,3,4])
    head = Solution().swapPairs(head)
    print_linked_list(head)