/*
 * Determine whether an integer is a palindrome. Do this without extra space.
 */

object PalindromeNumber
{
	def main(args: Array[String])
	{
		var input = 12344321
		var result = getPalindromeNumber(input)
		println(result)

		input = 12321
		result = getPalindromeNumber(input)
		println(result)

		input = 11
		result = getPalindromeNumber(input)
		println(result)

		input = 12343837
		result = getPalindromeNumber(input)
		println(result)

		input = 12343321
		result = getPalindromeNumber(input)
		println(result)

		input = -1
		result = getPalindromeNumber(input)
		println(result)
	}

	def getPalindromeNumber(input: Int): Boolean =
	{

		if (input < 0)
		{
			return false
		}

		var div = 1
		var tmpNum = input
		while(tmpNum / 10 != 0)
		{
			div = div * 10
			tmpNum = tmpNum / 10
		}

		var initNum = input
		while(true)
		{
			if (initNum < 10)
			{
				return true
			}
			val leftMost = initNum / div
			val rightMost = initNum % 10
			
			// println(f"Left: $leftMost -- Right: $rightMost")

			if (leftMost == rightMost)
			{
				initNum = initNum % div
				initNum = initNum / 10
				div = div / 10 / 10
			}
			else
			{
				return false
			}
		}

		return false
	}
}