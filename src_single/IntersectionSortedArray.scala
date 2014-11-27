/*
 * Find the intersection of two sorted arrays.
 */

object Intersection
{
    def main(args: Array[String])
    {
        var a1:Array[Int] = Array(0, 1, 2, 4, 5, 6, 7, 8, 12, 13)
        var a2:Array[Int] = Array(3, 4, 5, 6, 8, 10, 11, 12, 13, 14)
        println(intersect(a1, a2))
    }

    def intersect(a1: Array[Int], a2: Array[Int]): List[Int] =
    {
        var ret:List[Int] = List()
        var index_a1:Int = 0
        var index_a2:Int = 0
        var state:Boolean = true

        while(state)
        {
            if (a1(index_a1) == a2(index_a2))
            {
                ret = a1(index_a1) :: ret
                index_a1 = index_a1 + 1
                index_a2 = index_a2 + 1
            }
            else if (a1(index_a1) > a2(index_a2))
            {
                index_a2 = index_a2 + 1
            }
            else
            {
                index_a1 = index_a1 + 1
            }

            if (index_a1 == a1.length || index_a2 == a2.length)
            {
                state = false
            }

        }
        return ret
    }
}