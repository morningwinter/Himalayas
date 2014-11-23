/*
 * Given a string of lowercase characters, reorder them such that the same
 * characters are at least distance d from each other.
 */
import scala.util.control.Breaks._

object StringDistanceOrder
{
	def main(args: Array[String])
	{
		var input:String = "abb"
		println(input + ": " + solution(input, 2))

		input = "abbcc"
		println(input + ": " + solution(input, 2))

		input = "abbccddee"
		println(input + ": " + solution(input, 2))

		input = "aabb"
		println(input + ": " + solution(input, 3))

		input = "aaaabbbccceedd"
		println(input + ": " + solution(input, 2))

		input = "aaaabbbccceeddfghijklmn"
		println(input + ": " + solution(input, 5))

	}

	def solution(input: String, distance: Int): String =
	{
		// A map of character and counter.
		var map:Map[Char, Int] = Map()
		var length:Int = input.length()
		var ret:Array[Char] = new Array[Char](length)
		var pointer:Int = 0
		var maxDistance:Int = 0

		// Initial the Char array with '?'. For displaying only.
		for ( pos <- 0 to (length - 1) )
		{
			ret(pos) = '?'
		}

		// Build the map of character and its counter.
		for (pos <- 0 to length - 1)
		{
			var curChar:Char = input.charAt(pos)

			if (map.contains(curChar))
			{
				var count:Int = map(curChar) + 1
				map += (curChar -> count)
			}
			else
			{
				map += ( curChar -> 1 )
			}
		}

		// Sorting the Map in reverse order. '._2' means the second value
		// in the tuple. It returns a list of tuples.
		var result = map.toList sortWith {_._2 > _._2}

		for (item <- result)
		{
			var c:Char = item._1
			var count:Int = item._2
			var pos:Int = pointer

			// Count the maximum possible distance between the same Char.
			if (count > 1)
			{
				maxDistance = (length - 1)/( count - 1 )
			}

			// Insert the char into the ret array with maximum distance.
			for(i <- 1 to count)
			{
				if (pos > length -1)
				{
					pos = length - 1
				}

				// If the position has a letter already, then reduce the
				// position.
				while (ret(pos).isLetter)
				{
					pos -= 1
				}

				// Once we find a possible position to place the Char, check
				// if it a valid distance against the previous Char.
				for (i <- 1 to distance - 1)
				{
					var index:Int = pos - i
					if (index > 0 && ret(index) == c)
					{
						return "No Solution"
					}
				}

				// Place the Char and locate the next position based on the
				// maximum distance.
				ret(pos) = c
				pos += maxDistance
			}

			println("->" + ret.mkString)

			// Reset pointer to the first non-letter char when we move to
			// the next element in the map.
			breakable{
				for(pos <- 0 to length - 1)
				{
					if (! ret(pos).isLetter )
					{
						pointer = pos
						break
					}
				}
			}
		}

		return ret.mkString
	}
}