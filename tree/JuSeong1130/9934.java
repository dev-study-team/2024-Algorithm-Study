
문제풀이방법

root를 구하고 왼쪽 오른쪽을 나누고 다시 거기서 root를 구했어야 하는 문제였다.
start와 end를 이용해 계속해서 /2를 구해주면 root를 구할 수 있었고 이를 이용해 문제를 해결하였다.




import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.stream.Collectors;

public class Main {

    static Map<Integer,List<Integer>> result = new HashMap();
    static List<Integer> nums;
    static int K;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        K = sc.nextInt();
        sc.nextLine();
        nums = Arrays.stream(sc.nextLine().split(" "))
                .map(Integer::parseInt)
                .collect(Collectors.toList());
        for (int i = 0; i < K; i++) {
            result.put(i, new ArrayList<>());
        }
        calculateResult(0,0, nums.size() - 1);
        for (int i = 0; i < K; i++) {
            System.out.println(
                    result.get(i).stream()
                            .map(String::valueOf)
                            .collect(Collectors.joining(" "))
            );
        }
    }

    public static void calculateResult(int depth, int start, int end) {
        int root = (start + end) / 2;
        result.get(depth).add(nums.get(root));
        if(start == end) {
            return;
        }
        calculateResult(depth + 1, start, root - 1);
        calculateResult(depth + 1, root + 1, end);
    }


}
