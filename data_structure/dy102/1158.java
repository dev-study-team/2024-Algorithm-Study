import java.io.IOException;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Scanner;

public class Main {
    public List<Integer> solution(int count, int index) {
        List<Integer> arr = new ArrayList<>();
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < count; i++) {
            queue.add(i + 1);
        }
        int num = 1;
        while (queue.size() != 0) {
            if (num % index == 0) {
                arr.add(queue.poll());
                num++;
                continue;
            }
            queue.add(queue.poll());
            num++;
        }
        return arr;
    }

    public static void main(String[] args) throws IOException {
        Main main = new Main();
        Scanner scanner = new Scanner(System.in);
        int count = scanner.nextInt();
        int index = scanner.nextInt();
        List<Integer> arr = main.solution(count, index);
        String answer = arr.toString();
        answer = answer.replace('[', '<');
        answer = answer.replace(']', '>');
        System.out.println(answer);
    }
}
//꺼냈다가 넣고 꺼냈다가 넣고를 반복하는 방식을 어떻게 구현하지?를 고민하다가 위와 같이 구현했다.
//K번째 마다 꺼내기만 하고 넣지 않으면 큐에서 데이터들이 점점 사라진다.

//int num = 1;이어야 하는데 처음에 0으로 설정해서 애를 먹었다.
