from ..lib.linked_list import gen_linked_list_from_list, print_linked_list, ListNode

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        size = self.sizeof(head)
        if size == 0:
            return True
        elif size == 1:
            return True

        middle_index = size / 2
        if size % 2 == 1:
            odd = True
        else:
            odd = False

        l1 = head
        index = 0
        while index < middle_index:
            tmp_node = head
            head = head.next

            tmp_node.next = l1
            l1 = tmp_node
            index += 1

        if odd:
            head = head.next
              
        while l1 and head:
            if l1.val == head.val:
                l1 = l1.next
                head = head.next
            else:
                return False
        return True


    def sizeof(self, head):
        size = 0
        tmp = head
        while tmp:
            tmp = tmp.next
            size += 1
        return size

    def split_list(self, head, middle, odd):
        tmp = head
        index = 0
        while index < middle:
            index += 1
            if not odd:
                tmp = tmp.next
            elif odd and index != middle:
                tmp = tmp.next

        if odd:
            l2 = tmp.next.next
        else:
            l2 = tmp.next
        tmp.next = None
        return (head, l2)

    def reverse(self, head):
        new_head = head
        while head:
            tmp_node = head
            head = head.next

            tmp_node.next = new_head
            new_head = tmp_node
        return new_head



if __name__ == "__main__":
    head = gen_linked_list_from_list([1,2,3,2,1])
    print_linked_list(head)
    print Solution().isPalindrome(head)

    head = gen_linked_list_from_list([1,2,3,3,2,1])
    print_linked_list(head)
    print Solution().isPalindrome(head)

    head = gen_linked_list_from_list([1,2,3,3,2,1,1])
    print_linked_list(head)
    print Solution().isPalindrome(head)

    head = gen_linked_list_from_list([])
    print_linked_list(head)
    print Solution().isPalindrome(head)

    head = gen_linked_list_from_list([1])
    print_linked_list(head)
    print Solution().isPalindrome(head)

    head = gen_linked_list_from_list([1,1])
    print_linked_list(head)
    print Solution().isPalindrome(head)

    head = gen_linked_list_from_list([1,1,1])
    print_linked_list(head)
    print Solution().isPalindrome(head)

    head = gen_linked_list_from_list([1,1,1,2,1,1,1])
    print_linked_list(head)
    print Solution().isPalindrome(head)

    head = gen_linked_list_from_list([1,2,2,1])
    print_linked_list(head)
    print Solution().isPalindrome(head)

    head = gen_linked_list_from_list([1,1,2,1])
    print_linked_list(head)
    print Solution().isPalindrome(head)
