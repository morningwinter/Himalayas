# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def print_tree(root):
    if not root:
        print "NONE"
        return
    left_v = None
    right_v = None
    root_v = None
    if root.left:
        left_v = root.left.val
    if root.right:
        right_v = root.right.val
    if root:
        root_v = root.val
    print "(%s, %s, %s)" % (left_v, root_v, right_v)

    if root.left:
        print_tree(root.left)
    if root.right:
        print_tree(root.right)