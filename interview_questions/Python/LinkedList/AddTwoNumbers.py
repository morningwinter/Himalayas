from ..lib.linked_list import gen_linked_list_from_list, print_linked_list, ListNode

class Solution(object):

    def addTwoNumbers(self, l1, l2):
        l1_head = ListNode(None)
        l2_head = ListNode(None)
        return_head = l1_head

        l1_head.next = l1
        l2_head.next = l2

        carry = False
        while l1_head.next and l2_head.next:
            val = l1_head.next.val + l2_head.next.val
            if carry:
                carry = False
                val = val + 1

            if val >= 10:
                carry = True
                val = val - 10

            l1_head.next.val = val

            l1_head = l1_head.next
            l2_head = l2_head.next

        if l2_head.next:
            l1_head.next = l2_head.next

        while l1_head.next:
            val = l1_head.next.val
            if carry:
                carry = False
                val += 1

            if val >= 10:
                carry = True
                val = val - 10

            l1_head.next.val = val
            l1_head = l1_head.next

        if carry:
            l1_head.next = ListNode(1)

        return return_head.next



    def addTwoNumbers1(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        new_list = ListNode(None)
        new_head = new_list

        carry = False
        while l1 and l2:
            val = l1.val + l2.val
            if carry:
                carry = False
                val = val + 1

            if val >= 10:
                carry = True
                val = val - 10

            new_list.next = ListNode(val)

            l1 = l1.next
            l2 = l2.next
            new_list = new_list.next

        if l1:
            cur = l1
        else:
            cur = l2

        while cur:
            val = cur.val
            if carry:
                carry = False
                val = val + 1

            if val >= 10:
                carry = True
                val = val - 10
            new_list.next = ListNode(val)

            cur = cur.next
            new_list = new_list.next

        if carry:
            new_list.next = ListNode(1)

        return new_head.next


if __name__ == "__main__":
    l1 = gen_linked_list_from_list([0,1,2,3,4,5,6,7])
    l2 = gen_linked_list_from_list([0,1,2,3,4,5,6,7])
    head = Solution().addTwoNumbers(l1, l2)
    print_linked_list(head)

    l1 = gen_linked_list_from_list([0,1,2,3,4,5,6,7])
    l2 = gen_linked_list_from_list([3,4,5,6,7])
    head = Solution().addTwoNumbers(l1, l2)
    print_linked_list(head)

    l1 = gen_linked_list_from_list([0,1,2,3,4,5,6,7])
    l2 = gen_linked_list_from_list([3,4,5,6,7])
    head = Solution().addTwoNumbers(l2, l1)
    print_linked_list(head)

    l1 = gen_linked_list_from_list([])
    l2 = gen_linked_list_from_list([])
    head = Solution().addTwoNumbers(l1, l2)
    print_linked_list(head)

    l1 = gen_linked_list_from_list([1])
    l2 = gen_linked_list_from_list([])
    head = Solution().addTwoNumbers(l1, l2)
    print_linked_list(head)

    l1 = gen_linked_list_from_list([])
    l2 = gen_linked_list_from_list([1])
    head = Solution().addTwoNumbers(l1, l2)
    print_linked_list(head)

    l1 = gen_linked_list_from_list([1])
    l2 = gen_linked_list_from_list([1])
    head = Solution().addTwoNumbers(l1, l2)
    print_linked_list(head)

    l1 = gen_linked_list_from_list([9])
    l2 = gen_linked_list_from_list([9])
    head = Solution().addTwoNumbers(l1, l2)
    print_linked_list(head)

    l1 = gen_linked_list_from_list([1])
    l2 = gen_linked_list_from_list([9,9])
    head = Solution().addTwoNumbers(l1, l2)
    print_linked_list(head)