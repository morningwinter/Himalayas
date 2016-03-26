from ..lib.linked_list import gen_linked_list_from_list, print_linked_list, ListNode

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        new_head = ListNode(None)
        ptr = new_head
        new_head.next = head

        # NOTE: When using head.next, we can take the advantage of
        # both head and head.next as previous node and current node.
        while head.next:
            cur = head.next

            # NOTE: Only the smaller cur value need to be inserted.
            if head.val > cur.val:
            
                # Sort
                # NOTE: Only refresh the search pointer when
                # the cur val smaller (before) the pointer val.
                if cur.val < ptr.next.val:
                    ptr = new_head

                while ptr.next:
                    if ptr.next.val > cur.val:
                        next = cur.next
                        tmp = ptr.next
                        ptr.next = cur
                        cur.next = tmp
                        head.next = next
                        break
                    ptr = ptr.next
            else:
                head = head.next

        return new_head.next


if __name__ == "__main__":
    head = gen_linked_list_from_list([3,1,2])
    head = Solution().insertionSortList(head)
    print_linked_list(head)

    head = gen_linked_list_from_list([])
    head = Solution().insertionSortList(head)
    print_linked_list(head)

    head = gen_linked_list_from_list([1])
    head = Solution().insertionSortList(head)
    print_linked_list(head)

    head = gen_linked_list_from_list([1,2])
    head = Solution().insertionSortList(head)
    print_linked_list(head)

    head = gen_linked_list_from_list([2,1])
    head = Solution().insertionSortList(head)
    print_linked_list(head)

    head = gen_linked_list_from_list([1,2,3])
    head = Solution().insertionSortList(head)
    print_linked_list(head)

    head = gen_linked_list_from_list([3,2,1])
    head = Solution().insertionSortList(head)
    print_linked_list(head)

    head = gen_linked_list_from_list([3,1,2,4,5,99,4,9,4,2,6,3])
    head = Solution().insertionSortList(head)
    print_linked_list(head)