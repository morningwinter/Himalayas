

public class IntersectLinkedList {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode aPt = headA;
        ListNode bPt = headB;

        while (aPt != null && bPt != null)
        {
            if (aPt.val == bPt.val)
            {
                return aPt;
            }
            else if (aPt.val > bPt.val)
            {
                bPt = bPt.next;
            }
            else
            {
                aPt = aPt.next;
            }
        }

        return null;
    }

    public static void main(String[] args)
    {

        IntersectLinkedList intersectList = new IntersectLinkedList();
        int[] a = {0, 1, 2, 4, 5, 6, 7, 8, 12, 13};
        int[] b = {3, 4, 5, 6, 8, 10, 11, 12, 13, 14};
        ListNode headA = genList(a);
        ListNode headB = genList(b);
        ListNode intersectNode = intersectList.getIntersectionNode(headA, headB);
        System.out.println("Result: " + intersectNode.val);

        int[] a2 = {0, 1, 2, 4, 5};
        int[] b2 = {6, 8, 10, 11, 12, 13, 14};
        headA = genList(a2);
        headB = genList(b2);
        intersectNode = intersectList.getIntersectionNode(headA, headB);
        if (intersectNode == null)
        {
            System.out.println("Result: " + intersectNode);
        }
        else
        {
            System.out.println("Wrong Result: " + intersectNode.val);
        }

    }

    public static ListNode genList(int[] list)
    {
        ListNode head = new ListNode(list[0]);
        ListNode cur = head;
        for (int i = 1; i < list.length; i++)
        {
            cur.next = new ListNode(list[i]);
            cur = cur.next;
        }
        return head;
    }
}