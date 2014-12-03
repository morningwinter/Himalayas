import java.util.Hashtable;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;

public class ThreeSum {
    public List<List<Integer>> threeSum(int[] num) {
        Arrays.sort(num);

        List<List<Integer>> solutions = new ArrayList<List<Integer>>();

        int left = 0;
        int right = num.length - 1;

        if(right < 2)
            return solutions;

        while (num[left] <= 0 && left < num.length - 1)
        {
            int subSum = 0 - num[left];

            int middle = left + 1;
            while(middle < right)
            {
                int tmp = num[middle] + num[right];

                if (tmp > subSum)
                {
                    right--;
                }
                else if( tmp < subSum)
                {
                    middle++;
                }
                else
                {
                    ArrayList<Integer> solution = new ArrayList<Integer>();
                    solution.add(num[left]);
                    solution.add(num[middle]);
                    solution.add(num[right]);
                    int size = solutions.size();
                    if ( size > 0 )
                    {
                        List<Integer> preSolution = solutions.get(size - 1);
                        if (! (preSolution.get(0) == solution.get(0) && preSolution.get(1) == solution.get(1)))
                        {
                            solutions.add(solution);
                        }
                    }
                    else
                    {
                        solutions.add(solution);
                    }


                    right--;
                    middle++;
                }
            }

            right = num.length - 1;

            do
            {
               left++;
            }
            while (left < right - 1 && num[left] == num[left - 1]);

        }
        return solutions;
    } 

    public static void main(String[] args)
    {
        ThreeSum threeSum = new ThreeSum();

        int[] input = new int[]{-1, 0, 1, 2, -1, -4};
        List<List<Integer>> result = threeSum.threeSum(input);
        System.out.format("result: %s\n", result);

        input = new int[]{-1, -1, 0, 1, 1, 1};
        result = threeSum.threeSum(input);
        System.out.format("result: %s\n", result);

        input = new int[]{-10, -5, -6, -1, -1, 0, 1, 1, 1, 2, 6, 7, 8};
        result = threeSum.threeSum(input);
        System.out.format("result: %s\n", result);

        input = new int[]{-2, 0, 1, 1, 2};
        result = threeSum.threeSum(input);
        System.out.format("result: %s\n", result);

        input = new int[]{-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6};
        result = threeSum.threeSum(input);
        System.out.format("result: %s\n", result);   

        input = new int[]{0,1,2,2,2,3,3,4,4,6,6};
        result = threeSum.threeSum(input);
        System.out.format("result: %s\n", result); 

        input = new int[]{-1, -1, -2, -3, -4};
        result = threeSum.threeSum(input);
        System.out.format("result: %s\n", result); 

        input = new int[]{-1, -1, -1, -1, -1};
        result = threeSum.threeSum(input);
        System.out.format("result: %s\n", result); 

        input = new int[]{0,0,0};
        result = threeSum.threeSum(input);
        System.out.format("result: %s\n", result); 

    }
}