package mylib

class CyclicSortedList
{
	private var currentNode:Node = _
	private var size:Int = 0

	def addElement(num:Int) : Node =
	{
		var newNode : Node = new Node()
		newNode.setValue(num)

		if (currentNode == null)
		{
			currentNode = newNode
			currentNode.setNextNode(currentNode)
			size = size + 1
		}
		else
		{
			var isFound : Boolean = false
			var ptNode : Node = currentNode
			while (isFound == false)
			{
				var nextNode : Node = ptNode.getNextNode
				if (nextNode == currentNode)
				{
					isFound = true
				}
				// Regular case
				else if (ptNode.getValue <= num && nextNode.getValue > num)
				{
					isFound = true
				}
				// Tail
				else if (ptNode.getValue <= num && nextNode.getValue < num && nextNode.getValue < ptNode.getValue)
				{
					isFound = true
				}
				// Head
				else if (ptNode.getValue > num && nextNode.getValue >= num && nextNode.getValue < ptNode.getValue)
				{
					isFound = true
				}
				else
				{
					ptNode = ptNode.getNextNode
				}
			}

			var nextNode = ptNode.getNextNode
			newNode.setNextNode(nextNode)
			ptNode.setNextNode(newNode)
			currentNode = newNode
			size = size + 1
		}
		return newNode
	}

	def getCurrentNode: Node = currentNode

	/**
	 * Convert cyclic sorted list to an array
	 */
	def toArray() : Array[Int] = 
	{
		var nums : Array[Int] = new Array[Int](size)
		if (size != 0 )
		{
			var headNode : Node = findHeadNode()
			var ptNode : Node = headNode
			for (i <- 0 until size)
			{
				nums(i) = ptNode.getValue
				ptNode = ptNode.getNextNode
			}
		}
		return nums
	}

	/**
	 * Find the head node in the cyclic sorte list.
	 */
	def findHeadNode() : Node =
	{
		if (currentNode == null)
		{
			return null
		}
		var isFound : Boolean = false
		var headNode : Node = new Node()
		var ptNode : Node = currentNode
		while (isFound == false)
		{
			val thisValue = ptNode.getValue
			val nextNode = ptNode.getNextNode
			val nextValue = nextNode.getValue
			if (nextNode == currentNode)
			{
				headNode = currentNode
				isFound = true
			}
			else if (nextValue >= thisValue)
			{
				ptNode = nextNode
				isFound = false
			}
			else
			{
				headNode = nextNode
				isFound = true
			}
		}

		if (isFound)
		{
			return headNode
		}
		else
		{
			return null
		}
	}
}