import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
    public Integer solution(Stack<Integer> stack, String str) {
        if (str.contains("push")) {
            String num = str.replace("push ", "");
            stack.push(Integer.parseInt(num));
        }
        if ("pop".equals(str)) {
            if (stack.isEmpty()) {
                return -1;
            }
            return stack.pop();
        }
        if ("size".equals(str)) {
            return stack.size();
        }
        if ("empty".equals(str)) {
            if (stack.isEmpty()) {
                return 1;
            }
            return 0;
        }
        if ("top".equals(str)) {
            if (stack.isEmpty()) {
                return -1;
            }
            return stack.peek();
        }
        return 0;
    }

    public static void main(String[] args) throws IOException {
        Main main = new Main();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Stack<Integer> stack = new Stack<>();
        int x = Integer.parseInt(br.readLine());
        for (int i = 0; i < x; i++) {
            String str = br.readLine();
            Integer answer = main.solution(stack, str);
            if (str.contains("push")) {
                continue;
            }
            System.out.println(answer);
        }
    }
}
// 시간 초과가 떴는데 Scanner를 BufferedReader로 바꿔주니 해결됐다.
