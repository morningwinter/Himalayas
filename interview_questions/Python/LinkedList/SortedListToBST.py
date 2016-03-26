from ..lib.linked_list import gen_linked_list_from_list, print_linked_list, ListNode
from ..lib.tree import TreeNode, print_tree

class Solution(object):

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return head

        size = self.sizeof(head)
        root = self.convert(head, 0, size - 1)
        return root

    def convert(self, head, begin_index, end_index):
        if begin_index == end_index:
            return TreeNode(head.val)
        elif end_index - begin_index == 1:
            root = TreeNode(head.next.val)
            left = TreeNode(head.val)
            root.left = left
            return root

        offset = (end_index - begin_index + 1) / 2
        mid_index = begin_index + offset

        (_, mid, l2) = self.partition(head, offset)
        left = self.convert(head, begin_index, mid_index - 1)
        right = self.convert(l2, mid_index + 1, end_index)
        
        root = TreeNode(mid.val)
        root.left = left
        root.right = right
        return root
        

    def partition(self, head, mid_index):
        i = 0
        left = head
        while left:
            if i == mid_index - 1:
                mid = left.next
                # left.next = None
                right = mid.next
                # mid.next = None
                return  (left, mid, right)
            left = left.next
            i += 1

    def sizeof(self, head):
        size = 0
        tmp = head
        while tmp:
            tmp = tmp.next
            size += 1
        return size

if __name__ == "__main__":
    '''
    root = TreeNode(1)
    left = TreeNode(0)
    right = TreeNode(2)
    root.left = left
    root.right = right
    print_tree(root)
    '''

    head = gen_linked_list_from_list([1,2,3,4,5,6,7])
    root = Solution().sortedListToBST(head)
    print_tree(root)

    print
    head = gen_linked_list_from_list([])
    root = Solution().sortedListToBST(head)
    print_tree(root)

    print
    head = gen_linked_list_from_list([1])
    root = Solution().sortedListToBST(head)
    print_tree(root)

    print
    head = gen_linked_list_from_list([1,2])
    root = Solution().sortedListToBST(head)
    print_tree(root)

    print
    head = gen_linked_list_from_list([1,2,3])
    root = Solution().sortedListToBST(head)
    print_tree(root)

    print
    head = gen_linked_list_from_list([1,2,3,4])
    root = Solution().sortedListToBST(head)
    print_tree(root)

    print
    head = gen_linked_list_from_list([1,2,3,4,5])
    root = Solution().sortedListToBST(head)
    print_tree(root)

    print
    head = gen_linked_list_from_list([3,5,8])
    root = Solution().sortedListToBST(head)
    print_tree(root)
    print_linked_list(head)