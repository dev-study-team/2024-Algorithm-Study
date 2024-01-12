import java.io.IOException;
import java.util.Scanner;
import java.util.Stack;

public class Main {
    public void solution(int[] arr) {
        Stack<Integer> stack = new Stack<>();
        StringBuilder sb = new StringBuilder();
        int count = 1;
        int index = 0;
        while (true) {
            if (index > arr.length - 1) { //배열의 길이를 넘어서면, 완료된 것
                break;
            }
            if (count > arr.length + 1) { //주어진 수열의 수를 넘어서면, 잘못된 것
                System.out.println("NO");
                return;
            }
            if (stack.isEmpty() || stack.peek() != arr[index]) { //스택이 비거나(예외방지), 꺼내서 쓸 수 없는 상태일 때
                stack.push(count);
                count++;
                sb.append("+").append("\n");
            } else {
                stack.pop();
                index++;
                sb.append("-").append("\n");
            }
        }
        System.out.println(sb);
    }

    public static void main(String[] args) throws IOException {
        Main main = new Main();
        Scanner scanner = new Scanner(System.in);

        int x = Integer.parseInt(scanner.nextLine());
        int[] arr = new int[x];
        for (int i = 0; i < x; i++) {
            arr[i] = scanner.nextInt();
        }
        main.solution(arr);
    }
}
//특정 수가 꼭대기에 존재할 때까지 push. 이후에 pop

//어떤 원리인지는 파악하기 쉬웠으나, 예외를 처리하는 부분이 까다로웠음.
