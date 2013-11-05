/**
 * There are n coins in a line. (Assume n is even). Two players take turns to take a coin 
 * from one of the ends of the line until there are no more coins left. The player with the 
 * larger amount of money wins.
 *
 * Hint: Sum of the coins = sum of player A's coins + sum of player B's coins.
 */

 object CoinsInALine
 {
 	def main(args: Array[String])
 	{
 		var input: Array[Int] = Array(10,5,1,10,5,1)
 		println(getPossibleMaxSum(input, 0 , input.length - 1))
 		play(input)
 	}

 	def play(coins:Array[Int])
 	{
 		var playerA : Boolean = true
 		var ptLeft : Int = 0
 		var ptRight : Int = coins.length - 1

 		while(ptLeft <= ptRight)
 		{
 			if (ptLeft == ptRight - 1)
 			{
 				var leftCoin:Int = coins(ptLeft)
 				var rightCoin:Int = coins(ptRight)
 				if(leftCoin > rightCoin)
 				{
 					var player : String = getPlayer(playerA)
 					println(f"Player: $player. Pick left: $leftCoin")
 					playerA = !playerA
 					player = getPlayer(playerA)
 					println(f"Player: $player. Pick right: $rightCoin")
 				}
 				else
 				{
 					var player : String = getPlayer(playerA)
 					println(f"Player: $player. Pick rght: $rightCoin")
 					playerA = !playerA
 					player = getPlayer(playerA)
 					println(f"Player: $player. Pick left: $leftCoin")
 				}
 				return
 			}
 			var maxSumRight : Int = getPossibleMaxSum(coins, ptLeft + 1, ptRight)
 			var maxSumLeft : Int = getPossibleMaxSum(coins, ptLeft, ptRight - 1)
 			if (maxSumRight > maxSumLeft)
 			{
 				var rightCoin : Int = coins(ptRight)
 				var player : String = getPlayer(playerA)
 				println(f"Player: $player. Pick right: $rightCoin")
 				ptRight = ptRight - 1

 			}
 			else
 			{
 				var leftCoin : Int = coins(ptLeft)
 				var player : String = getPlayer(playerA)
 				println(f"Player: $player. Pick left: $leftCoin")
 				ptLeft = ptLeft + 1
 			}
 			playerA = !playerA
 		} 
 	}

 	// Return the maximum possible sum between index ptLeft and index ptRight
 	def getPossibleMaxSum(input: Array[Int], ptLeft: Int, ptRight: Int): Int =
 	{
 		// Base case
 		if (ptLeft == ptRight - 1)
 		{
 			var left:Int = input(ptLeft)
 			var right:Int = input(ptRight)
 			if (left > right)
 			{
 				return left
 			}
 			else
 			{
 				return right
 			}
 		}

 		var _sum : Int = sum(input, ptLeft, ptRight)

 		// Max sum for one player = sum - max sum for the opposite player (taking the left coin out).
 		var maxLeft = _sum - getPossibleMaxSum(input, ptLeft + 1, ptRight)

 		// Max sum for one player = sum - max sum for the oppostie player. (taking the right coin out).
 		var maxRight = _sum - getPossibleMaxSum(input, ptLeft, ptRight - 1)


 		if (maxLeft > maxRight)
 		{
 			return maxLeft
 		}
 		else
 		{
 			return maxRight
 		}
 	}

 	def sum(input: Array[Int], start:Int, end:Int): Int =
 	{
 		var ret : Int = 0
 		for (i <- start until end + 1)
 		{
 			ret = ret + input(i)
 		}
 		return ret
 	}

 	def getPlayer(playerA : Boolean) : String =
 	{
 		if (playerA)
 		{
 			return "Player A"
 		}
 		else
 		{
 			return "Player B"
 		}
 	}
 }
