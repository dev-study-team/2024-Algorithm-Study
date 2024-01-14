import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
    public String solution(String str) {
        Stack<Character> stack = new Stack<>();
        char[] arr = str.toCharArray();
        for (char c : arr) {
            if (c == '(') {
                stack.push(c);
            } else {
                if (stack.isEmpty()) {
                    return "NO";
                }
                stack.pop();
            }
        }
        if (stack.size() != 0) {
            return "NO";
        }
        return "YES";
    }

    public static void main(String[] args) throws IOException {
        Main main = new Main();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int x = Integer.parseInt(br.readLine());
        for (int i = 0; i < x; i++) {
            String str = br.readLine();
            System.out.println(main.solution(str));
        }
    }
}
