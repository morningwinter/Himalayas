from ..lib.linked_list import gen_linked_list_from_list, print_linked_list, ListNode

class Solution(object):
    def sortList(self, head):
        if not head or head.next is None:
            return head
        (head, tail) = self.quick_sort(head)
        return head

    def quick_sort(self, head):
        if head is None or head.next is None:
            return (head, head)

        (head1, tail1, mid_head, mid_tail, head2, tail2) = self.partition(head)

        (head1, tail1) = self.quick_sort(head1)
        (head2, tail2) = self.quick_sort(head2)

        if tail1 is not None:
            tail1.next = mid_head
        else:
            head1 = mid_head
        mid_tail.next = head2

        if head2 is None:
            tail2 = mid_tail
        
        return head1, tail2


    def partition(self, head):
        head1 = ListNode(None)
        head2 = ListNode(None)
        mid_head = ListNode(None)

        tail1 = head1
        tail2 = head2
        mid_tail = mid_head

        pivot = head.val
        ptr = head
        while ptr:
            if ptr.val < pivot:
                tail1.next = ptr
                tail1 = ptr 
            elif ptr.val > pivot:
                tail2.next = ptr
                tail2 = ptr
            else:
                mid_tail.next = ptr
                mid_tail = ptr
            ptr = ptr.next

        tail1.next = None
        tail2.next = None
        mid_tail.next = None

        return (head1.next, tail1, mid_head.next, mid_tail, head2.next, tail2)


    def sortList1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        size = self.sizeof(head)
        if size <= 1:
            return head

        head = self.merge_sort(head, 0, size - 1)
        return head

    def merge_sort(self, head, begin_index, end_index):
        if begin_index == end_index:
            # print 'Bottom: %s, %s' % (begin_index, head.val)
            head.next = None
            return head
        
        mid_index = begin_index + (end_index - begin_index) / 2

        # print "Mid Idx: %s %s %s " % (begin_index, mid_index, end_index)
        mid_node = self.element_at(head, mid_index - begin_index)
        tmp = mid_node.next
        mid_node.next = None

        l1 = self.merge_sort(head, begin_index, mid_index)
        l2 = self.merge_sort(tmp, mid_index + 1, end_index)
        head = self.merge(l1, l2)

        return head

    def merge(self, l1, l2):
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

    def sizeof(self, head):
        size = 0
        tmp = head
        while tmp:
            tmp = tmp.next
            size += 1
        return size

    def element_at(self, head, index):
        tmp = head
        i = 0
        while i < index:
            tmp = tmp.next
            i += 1
        return tmp


if __name__ == "__main__":

    head = gen_linked_list_from_list([2,1])
    head = Solution().sortList(head)
    print_linked_list(head)
    
    head = gen_linked_list_from_list([1,2,3,4,5])
    head = Solution().sortList(head)
    print_linked_list(head)

    head = gen_linked_list_from_list([2,1])
    head = Solution().sortList(head)
    print_linked_list(head)

    head = gen_linked_list_from_list([5,4,3,2,1])
    head = Solution().sortList(head)
    print_linked_list(head)

    head = gen_linked_list_from_list([1,3,2])
    head = Solution().sortList(head)
    print_linked_list(head)

    head = gen_linked_list_from_list([1,3,4,6,2])
    head = Solution().sortList(head)
    print_linked_list(head)

    head = gen_linked_list_from_list([1,4,3,2,4,3,1])
    head = Solution().sortList(head)
    print_linked_list(head)

    head = gen_linked_list_from_list([1,4,3,2,4,3,1,100,98,55,1,200])
    head = Solution().sortList(head)
    print_linked_list(head)

    head = gen_linked_list_from_list([1,4,3,2,4,3,-1,100,98,55,1,-199,200])
    head = Solution().sortList(head)
    print_linked_list(head)
