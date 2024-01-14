import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Deque;
import java.util.LinkedList;

public class Main {
    public Integer solution(int x) {
        Deque<Integer> deque = new LinkedList<>();
        for (int i = 1; i <= x; i++) {
            deque.addLast(i);
        }
        while (deque.size() != 1) {
            deque.removeFirst();
            deque.addLast(deque.getFirst());
            deque.removeFirst();
        }
        return deque.getFirst();
    }

    public static void main(String[] args) throws IOException {
        Main main = new Main();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int x = Integer.parseInt(br.readLine());
        System.out.println(main.solution(x));
    }
}
