import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Deque;
import java.util.LinkedList;
import java.util.List;

public class Main {
    public List<Integer> solution(String[] str) {
        Deque<Integer> deque = new LinkedList<>();
        List<Integer> arr = new ArrayList<>();
        for (int i = 0; i < str.length; i++) {
            if (str[i].contains("push_front")) {
                str[i] = str[i].replaceAll("[^0-9]", "");
                deque.addFirst(Integer.parseInt(str[i]));
            } else if (str[i].contains("push_back")) {
                str[i] = str[i].replaceAll("[^0-9]", "");
                deque.addLast(Integer.parseInt(str[i]));
            } else if (str[i].equals("pop_front")) {
                if (deque.isEmpty()) {
                    arr.add(-1);
                    continue;
                }
                arr.add(deque.removeFirst());
            } else if (str[i].equals("pop_back")) {
                if (deque.isEmpty()) {
                    arr.add(-1);
                    continue;
                }
                arr.add(deque.removeLast());
            } else if (str[i].equals("size")) {
                arr.add(deque.size());
            } else if (str[i].equals("empty")) {
                if (deque.isEmpty()) {
                    arr.add(1);
                    continue;
                }
                arr.add(0);
            } else if (str[i].equals("front")) {
                if (deque.isEmpty()) {
                    arr.add(-1);
                    continue;
                }
                arr.add(deque.getFirst());
            } else if (str[i].equals("back")) {
                if (deque.isEmpty()) {
                    arr.add(-1);
                    continue;
                }
                arr.add(deque.getLast());
            }
        }
        return arr;
    }

    public static void main(String[] args) throws IOException {
        Main main = new Main();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int x = Integer.parseInt(br.readLine());
        String[] arr = new String[x];
        for (int i = 0; i < x; i++) {
            arr[i] = br.readLine();
        }
        List<Integer> answer = main.solution(arr);
        for (int i : answer) {
            System.out.println(i);
        }
    }
}
//하나씩 받아서하면 시간초과 발생. 배열로 받아서 한꺼번에 처리
