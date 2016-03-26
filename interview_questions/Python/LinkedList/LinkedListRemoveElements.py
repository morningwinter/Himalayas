from ..lib.linked_list import gen_linked_list_from_list, print_linked_list

class Solution(object): 
    def removeElements1(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        ptr = head
        pre = head
        while ptr:
            if ptr.val == val:
                if ptr.next:
                    ptr.val = ptr.next.val
                    ptr.next = ptr.next.next
                else:
                    pre.next = None
                    if ptr.val == head.val:
                        head = None
                    ptr = None
            else:
                pre = ptr
                ptr = ptr.next

        return head

    def removeElements2(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        ptr = head
        pre = head
        while ptr:
            if ptr.val == val:
                if ptr.val == pre.val:
                    # Removing element from head.
                    ptr = ptr.next
                    pre = ptr
                    head = head.next
                else:
                    # Removing element from body.
                    pre.next = ptr.next
                    ptr = ptr.next

            else:
                # Moving the pointers.
                pre = ptr
                ptr = ptr.next

        return head

    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        start = head
        end = head

        while end and end.val == val:
            end = end.next
        start = end
        head = end

        found = False
        while end:
            if end.val == val:
                if not found:
                    found = True
                end = end.next
            elif end.val != val and found:
                found = False
                start.next = end
                start = end
                end = end.next
            else:
                start = end
                end = end.next

        if end is None and found:
            start.next = None

        return head


if __name__ == "__main__":
    head = gen_linked_list_from_list([0,1,2,3,4])
    print_linked_list(head)
    Solution().removeElements(head, 3)
    print_linked_list(head)

    print '=========='
    head = gen_linked_list_from_list([0,1,2,3,4])
    print_linked_list(head)
    head = Solution().removeElements(head, 0)
    print_linked_list(head)
    head = Solution().removeElements(head, 4)
    print_linked_list(head)

    print '=========='
    head = gen_linked_list_from_list([0,0,1,2,0,3,4,0,0])
    print_linked_list(head)
    head = Solution().removeElements(head, 0)
    print_linked_list(head)

    print '=========='
    head = gen_linked_list_from_list([1,2,1,2])
    print_linked_list(head)
    head = Solution().removeElements(head, 2)
    print_linked_list(head)


    print '=========='
    head = gen_linked_list_from_list([1,1,1,1,1])
    print_linked_list(head)
    head = Solution().removeElements(head, 1)
    print_linked_list(head)

    head = gen_linked_list_from_list([1])
    print_linked_list(head)
    head = Solution().removeElements(head, 1)
    print_linked_list(head)

    head = gen_linked_list_from_list([1,1])
    print_linked_list(head)
    head = Solution().removeElements(head, 1)
    print_linked_list(head)