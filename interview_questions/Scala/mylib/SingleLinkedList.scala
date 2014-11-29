package mylib

class SingleLinkedList
{
    private var headNode:Node = _
    private var tailNode:Node = _
    private var currentNode:Node = _
    private var size:Int = 0

    def addElement(num:Int) : Node =
    {
        var newNode : Node = new Node()
        newNode.setValue(num)

        if (currentNode == null)
        {
            currentNode = newNode
            headNode = newNode
            size = size + 1
        }
        else
        {
            currentNode.setNextNode(newNode)
            currentNode = newNode
            tailNode = newNode
            size = size + 1
        }
        return newNode
    }

    def getHeadNode:Node = headNode

    def getTailNode:Node = tailNode

    def reverseIteration() =
    {
        var cur:Node = headNode
        var pre:Node = null
        var next:Node = null

        var state:Boolean = true

        while(cur != null)
        {
            next = cur.getNextNode
            cur.setNextNode(pre)
            pre = cur
            cur = next
        }
        headNode = pre
    }

    def reverseRecursive() =
    {
        doReverseRecursive(headNode)
    }

    def doReverseRecursive(node:Node): Unit =
    {
        if (node == null)
        {
            return
        }

        var next: Node = node.getNextNode
        if (next == null)
        {
            node.setNextNode(null)
            headNode = node
            return
        }

        doReverseRecursive(next)
        next.setNextNode(node)
    }

    /**
     * Make String.
     */
    def mkString : String = 
    {
        var retString : String = ""
        if (size != 0 )
        {
            var headNode : Node = getHeadNode
            var ptNode : Node = headNode
            for (i <- 0 until size)
            {
                retString = retString + " " + ptNode.getValue
                ptNode = ptNode.getNextNode
            }
        }
        return retString
    }

}