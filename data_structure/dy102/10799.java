import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
    public int solution(String str) {
        char[] arr = str.toCharArray();
        Stack<Character> stack = new Stack<>();
        int total = 0; //총 쇠막대기의 수
        int count = 0; //현재 위치에서 자를 수 있는 쇠막대기의 수
        int answer = 0;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == '(') {
                if (arr[i + 1] == ')') {
                    answer += count;//레이저로 컷해서 추가로 얻은 막대기 수
                    continue;
                }
                stack.push('(');
                count++;
                total++;
            } else {
                if (arr[i - 1] == '(') {
                    continue;
                }
                stack.push(')');
                count--;
            }
        }
        return answer + total;
    }

    public static void main(String[] args) throws IOException {
        Main main = new Main();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String str = br.readLine();
        System.out.println(main.solution(str));
    }
}

//()면 레이저. 그 전에 있는 (( 들은 모두 누적해서 계산한다.(그 전에 ')'가 존재한다면 누적된 수를 줄인다.)
//레이저가 존재하는 위치에서 누적된 막대기의 수만큼 더하면 된다.

//주의할 점: 잘라서 얻은 수만큼만 더하고 있으므로, 마지막에 총 막대기의 수를 더해줘야 한다.
