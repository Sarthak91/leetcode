import java.util.*;
/*
*    This class
*/
public class TwoSum {
    public static int[] num(int[] arr, int target){
        Map<Integer,Integer> map = new HashMap<>();
        int[] res = new int[2];
        for(int i: arr) {
             map.put(i,arr[i]);
         }
        for (int i = 0; i < arr.length; i++) {
            int complement = target - arr[i];
            if (map.containsValue(complement)&& map.get(complement) != i){
                return new int[] {i,map.get(complement)};
            }
        }
        throw new IllegalArgumentException("No two sum solution");
    }
    public static  void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter array length");
        int numLen = sc.nextInt();
        int[] result = new int[2];
        int[] inArray = new int[10];
        for (int i = 0; i < numLen ; i++) {
            System.out.println("enter  array values");
                inArray[i]  = sc.nextInt();
        }
        System.out.println("Enter Target");
        int target =  sc.nextInt();
        result = num(inArray,target);
        for(int val: result) {
            System.out.println(result[val]);
        }
        }
    }
