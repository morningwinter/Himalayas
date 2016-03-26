from ..lib.linked_list import gen_linked_list, print_linked_list

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        odd_ptr = None
        even_start_ptr = None
        even_ptr = None
        node_ptr = head

        if node_ptr:
            odd_ptr = node_ptr
            node_ptr = node_ptr.next
            even_ptr = node_ptr
            even_start_ptr = node_ptr
            if node_ptr:
                node_ptr = node_ptr.next

        while node_ptr:
            odd_ptr.next = node_ptr
            odd_ptr = odd_ptr.next
            node_ptr = node_ptr.next

            even_ptr.next = node_ptr
            even_ptr = even_ptr.next
            if node_ptr:
                node_ptr = node_ptr.next

        if odd_ptr:
            odd_ptr.next = even_start_ptr

        return head


if __name__ == "__main__":
    head = gen_linked_list(7)  
    print_linked_list(head)
    print_linked_list(Solution().oddEvenList(head))
    print

    head = gen_linked_list(0)  
    print_linked_list(head)
    print_linked_list(Solution().oddEvenList(head))
    print

    head = gen_linked_list(1)  
    print_linked_list(head)
    print_linked_list(Solution().oddEvenList(head))
    print

    head = gen_linked_list(2)  
    print_linked_list(head)
    print_linked_list(Solution().oddEvenList(head))
    print

    head = gen_linked_list(3)  
    print_linked_list(head)
    print_linked_list(Solution().oddEvenList(head))
    print

    head = gen_linked_list(4)  
    print_linked_list(head)
    print_linked_list(Solution().oddEvenList(head))
    print