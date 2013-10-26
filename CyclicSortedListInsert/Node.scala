class Node
{
	// '_' means default value here.
	private var _nextNode : Node = _
	private var _value : Int = 0

	def getNextNode = _nextNode

	def setNextNode(node:Node):Unit = 
	{
		_nextNode = node
	}

	def getValue = _value

	def setValue(value:Int):Unit =
	{
		_value = value
	}
}