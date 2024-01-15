import java.io.IOException;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Scanner;
import java.util.stream.Collectors;

public class Main {
    public Integer solution(int index, List<Integer> arr) {
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < arr.size(); i++) {
            queue.add(i);//문서 목록(0,1,2...)
        }
        List<Integer> sortedArr = arr.stream().sorted((a, b) -> b - a)
                .collect(Collectors.toList());//중요도의 최댓값 찾기
        int count = 1;
        while (true) {
            if (arr.get(queue.peek()) == sortedArr.get(0)) {//최댓값을 가졌는지 확인한다.
                sortedArr.remove(0);//최댓값인 경우 제거하고, 큐에서도 제거한다.
                if (queue.peek() == index) {
                    return count;
                }
                queue.poll();
                count++;
                continue;
            }
            queue.add(queue.poll());
        }
    }

    public static void main(String[] args) throws IOException {
        Main main = new Main();
        Scanner scanner = new Scanner(System.in);

        int x = Integer.parseInt(scanner.nextLine());
        List<Integer> arr = new ArrayList<>();
        int count;
        int index = 0;
        for (int i = 0; i < x; i++) {
            arr.clear();
            count = scanner.nextInt();
            index = scanner.nextInt();
            for (int j = 0; j < count; j++) {
                arr.add(scanner.nextInt());
            }
            System.out.println(main.solution(index, arr));
        }
    }
}
//중요도를 어떻게 각각의 문서마다 할당해줄 수 있는지에 대해 많이 고민했다. -> 실시간으로 변하는 최댓값을 어떻게 해결할것인가.
//내림차순 정렬된 배열과 기존의 배열을 비교하는 방식으로 해결했다. (.remove(0) 꿀팁)

//continue를 안 붙이고 있었음
//내림차순 배열 만들어야하는데 오름차순 만듦
