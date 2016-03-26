from ..lib.linked_list import gen_linked_list_from_list, print_linked_list, ListNode

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)

        tmp_node = head
        while l1 and l2:    
            if l1.val < l2.val:
                tmp_node.next = l1
                l1 = l1.next
            else:
                tmp_node.next = l2
                l2 = l2.next
            tmp_node = tmp_node.next

        if l1:
            tmp_node.next = l1
        elif l2:
            tmp_node.next = l2

        return head.next


if __name__ == "__main__":
    l1 = gen_linked_list_from_list([0,1,2,3,4,5,6,7])
    l2 = gen_linked_list_from_list([0,1,2,3,4,5,6,7])
    head = Solution().mergeTwoLists(l1, l2)
    print_linked_list(head)

    l1 = gen_linked_list_from_list([])
    l2 = gen_linked_list_from_list([])
    head = Solution().mergeTwoLists(l1, l2)
    print_linked_list(head)


    l1 = gen_linked_list_from_list([0])
    l2 = gen_linked_list_from_list([])
    head = Solution().mergeTwoLists(l1, l2)
    print_linked_list(head)

    l1 = gen_linked_list_from_list([])
    l2 = gen_linked_list_from_list([0])
    head = Solution().mergeTwoLists(l1, l2)
    print_linked_list(head)

    l1 = gen_linked_list_from_list([0])
    l2 = gen_linked_list_from_list([0])
    head = Solution().mergeTwoLists(l1, l2)
    print_linked_list(head)

    l1 = gen_linked_list_from_list([0,1])
    l2 = gen_linked_list_from_list([0,1])
    head = Solution().mergeTwoLists(l1, l2)
    print_linked_list(head)

    l1 = gen_linked_list_from_list([0,1,2,3])
    l2 = gen_linked_list_from_list([100,101,102])
    head = Solution().mergeTwoLists(l1, l2)
    print_linked_list(head)

    l1 = gen_linked_list_from_list([0,1,2,3,199])
    l2 = gen_linked_list_from_list([100,101,102])
    head = Solution().mergeTwoLists(l1, l2)
    print_linked_list(head)
