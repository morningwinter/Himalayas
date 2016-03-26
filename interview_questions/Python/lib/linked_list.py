def print_linked_list(head):
    node = head
    if not head:
        print 'NONE'
        return

    while node:
        print " ->%s" % node.val,
        node = node.next
    print


def gen_linked_list(size):
    head = None
    if size:
        for i in range(0, size):
            tmp_node = head
            head = ListNode(i)
            head.next = tmp_node
    return head

def gen_linked_list_from_list(input_array):
    head = None
    ptr = None
    if input_array:
        index = 0
        for item in input_array:
            if index == 0:
                head = ListNode(item)
                ptr = head
            else:
                tmp_node = ListNode(item)
                ptr.next = tmp_node
                ptr = ptr.next
            index += 1

    return head


def node_at(head, index):
    i = 0;
    prt = head
    while prt:
        if i == index:
            return prt
        i = i + 1
        prt = prt.next
            


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None