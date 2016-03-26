from ..lib.linked_list import gen_linked_list, print_linked_list, node_at

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_head = None
        while head:
            tmp_node = head
            head = tmp_node.next
            tmp_node.next = new_head 
            new_head = tmp_node

        return new_head

    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node:
            if node.next:
                node.val = node.next.val
                node.next = node.next.next


if __name__ == "__main__":

    # Reverse List
    print '===== Reverse List ====='
    head = gen_linked_list(7)  
    print_linked_list(head)
    print_linked_list(Solution().reverseList(head))
    print

    head = gen_linked_list(0)  
    print_linked_list(head)
    print_linked_list(Solution().reverseList(head))
    print

    head = gen_linked_list(1)  
    print_linked_list(head)
    print_linked_list(Solution().reverseList(head))
    print

    head = gen_linked_list(2)  
    print_linked_list(head)
    print_linked_list(Solution().reverseList(head))
    print

    print '===== Delete Node From List ====='
    head = gen_linked_list(7)
    print_linked_list(head)
    node = node_at(head, 5)
    Solution().deleteNode(node)
    print_linked_list(head)
    node = node_at(head, 0)
    Solution().deleteNode(node)
    print_linked_list(head)

    head = gen_linked_list(2)
    print_linked_list(head)
    node = node_at(head, 0)
    Solution().deleteNode(node)
    print_linked_list(head)

    head = gen_linked_list(1)
    print_linked_list(head)
    node = node_at(head, 0)
    Solution().deleteNode(node)
    print_linked_list(head)
