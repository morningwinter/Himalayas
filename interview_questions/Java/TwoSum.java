import java.util.Hashtable;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;

public class TwoSum {
    public int[] twoSum(int[] numbers, int target) {
        Hashtable<Integer, List<Integer>> table = new Hashtable();
        int[] solution = new int[2];

        for (int i = 0 ; i < numbers.length; i++)
        {
            if (table.get(numbers[i]) == null)
            {
                List list = new ArrayList<Integer>();
                list.add(i);
                table.put(numbers[i], list);
            }
            else
            {
                List list = table.get(numbers[i]);
                list.add(i);
            }
        }

        System.out.println(table.toString());

        for (int i = 0; i < numbers.length; i++)
        {
            int numX = numbers[i];
            int numY = target - numbers[i];
            List<Integer> indexs = table.get(numY);
            if (indexs != null)
            {
                if (numX != numY)
                {
                    solution[0] = i + 1;
                    solution[1] = indexs.get(0) + 1;
                }
                else if (indexs.size() > 1)
                {
                    solution[0] = indexs.get(0) + 1;
                    solution[1] = indexs.get(1) + 1;
                }
            }
        }

        Arrays.sort(solution);
        return solution;
    } 

    public static void main(String[] args)
    {
        TwoSum twoSum = new TwoSum();

        int[] input1 = {2, 7, 11, 15};
        int[] result = twoSum.twoSum(input1, 9);
        System.out.format("index1=%d, inex2=%d\n", result[0], result[1]);

        input1 = new int[]{1, 2, 7, 11, 15, 18, 20, 21};
        result = twoSum.twoSum(input1, 29);
        System.out.format("index1=%d, inex2=%d\n", result[0], result[1]);

        input1 = new int[]{1, 2, 7, 11, 15, 18, 20, 21};
        result = twoSum.twoSum(input1, 100);
        System.out.format("index1=%d, inex2=%d\n", result[0], result[1]);

        input1 = new int[]{0,4,3,0};
        result = twoSum.twoSum(input1, 0);
        System.out.format("index1=%d, inex2=%d\n", result[0], result[1]);

        input1 = new int[]{5, 75, 25};
        result = twoSum.twoSum(input1, 100);
        System.out.format("index1=%d, inex2=%d\n", result[0], result[1]);
    }
}