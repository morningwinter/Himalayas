/*
  Implement the reversal of a singly linked list iteratively and recursively.
*/

import mylib.SingleLinkedList

object ReverseLinkedList
{
    def main(args: Array[String])
    {
        var list:SingleLinkedList = new SingleLinkedList()
        list.addElement(1)
        list.addElement(2)
        list.addElement(3)
        list.addElement(4)
        list.addElement(5)
        do_reverse(list)

        list = new SingleLinkedList()
        do_reverse(list)

        list = new SingleLinkedList()
        list.addElement(1)
        do_reverse(list)

        list = new SingleLinkedList()
        list.addElement(1)
        list.addElement(2)
        do_reverse(list)

        list = new SingleLinkedList()
        list.addElement(1)
        list.addElement(2)
        list.addElement(3)
        do_reverse(list)


    }

    def do_reverse(list:SingleLinkedList)
    {
        println(list.mkString)
        list.reverseIteration
        println(list.mkString)
        list.reverseRecursive
        println(list.mkString)
        println()
    }
}