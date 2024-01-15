import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.Stack;

public class Main {
    public Double solution(String str, int[] arr) {
        Stack<Double> stack = new Stack<>();
        Map<Character, Integer> map = new HashMap<>();
        int x = 65;
        for (int j : arr) {
            map.put((char) x, j);
            x++;
        }
        char[] arr2 = str.toCharArray();
        for (char c : arr2) {
            if (Character.isAlphabetic(c)) {
                stack.push((double) map.get(c));
                continue;
            }
            double num1 = stack.pop();
            double num2 = stack.pop();
            if (c == '*') {
                stack.push(num2 * num1);
            }
            else if (c == '+') {
                stack.push(num2 + num1);
            }
            else if (c == '-') {
                stack.push(num2 - num1);
            }
            else if (c == '/') {
                stack.push(num2 / num1);
            }
        }
        return stack.pop();
    }

    public static void main(String[] args) throws IOException {
        Main main = new Main();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int x = Integer.parseInt(br.readLine());
        String str = br.readLine();
        int[] arr = new int[x];

        for (int i = 0; i < x; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }
