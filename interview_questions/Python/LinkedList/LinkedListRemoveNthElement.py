from ..lib.linked_list import gen_linked_list_from_list, print_linked_list

class Solution(object): 
    def removeNthFromEnd1(self, head, n):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        store = []

        if n <= 0:
            return head

        ptr_node = head
        while ptr_node:
            store.append(ptr_node)
            ptr_node = ptr_node.next

        total_size = len(store)
        index = total_size - n

        if index == 0:
            head = head.next
        elif index > 0:
            node = store[index]
            pre_node = store[index - 1]
            pre_node.next = node.next

        return head

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if n <= 0:
            return head

        mark_node = head
        ptr_node = head

        i = 0
        while ptr_node:
            if i > n:
                mark_node = mark_node.next

            i = i + 1
            ptr_node = ptr_node.next


        if n == i:
            head = head.next
        elif n < i:
            mark_node.next = mark_node.next.next

        return head



if __name__ == "__main__":
    head = gen_linked_list_from_list([0,1,2,3,4,5,6,7])
    print_linked_list(head)
    head = Solution().removeNthFromEnd(head, 3)
    print_linked_list(head)
    head = Solution().removeNthFromEnd(head, 1)
    print_linked_list(head)
    head = Solution().removeNthFromEnd(head, 6)
    print_linked_list(head)
    head = Solution().removeNthFromEnd(head, 0)
    print_linked_list(head)
    head = Solution().removeNthFromEnd(head, 7)
    print_linked_list(head)
    head = Solution().removeNthFromEnd(head, 1)
    print_linked_list(head)
    head = Solution().removeNthFromEnd(head, 1)
    print_linked_list(head)
    head = Solution().removeNthFromEnd(head, 1)
    print_linked_list(head)
    head = Solution().removeNthFromEnd(head, 1)
    print_linked_list(head)
    head = Solution().removeNthFromEnd(head, 1)
    print_linked_list(head)
    head = Solution().removeNthFromEnd(head, 1)
    print_linked_list(head)


    head = gen_linked_list_from_list([0,1,2,3])
    print_linked_list(head)
    head = Solution().removeNthFromEnd(head, 4)
    print_linked_list(head)
    head = Solution().removeNthFromEnd(head, 3)
    print_linked_list(head)
    head = Solution().removeNthFromEnd(head, 2)
    print_linked_list(head)
    head = Solution().removeNthFromEnd(head, 1)
    print_linked_list(head)
    head = Solution().removeNthFromEnd(head, 0)
    print_linked_list(head)