object Main
{
	def main(args:Array[String])
	{
	
		var nodeList : CyclicSortedList = new CyclicSortedList()
		nodeList.addElement(5)
		nodeList.addElement(8)
		nodeList.addElement(6)
		nodeList.addElement(11)
		nodeList.addElement(3)
		nodeList.addElement(10)
		nodeList.addElement(9)
		printArray(nodeList.toArray)

		nodeList = new CyclicSortedList()
		nodeList.addElement(1)
		nodeList.addElement(1)
		nodeList.addElement(1)
		nodeList.addElement(5)
		printArray(nodeList.toArray)

		nodeList = new CyclicSortedList()
		nodeList.addElement(9)
		nodeList.addElement(9)
		nodeList.addElement(9)
		nodeList.addElement(1)
		printArray(nodeList.toArray)

	}

	def printArray(arr: Array[Int])
	{
		for (num <- arr)
		{
			println(f"$num")
		}
		println("==========")
	}
}