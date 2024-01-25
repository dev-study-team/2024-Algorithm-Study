https://www.acmicpc.net/problem/2696

참고
https://steady-coding.tistory.com/88
https://velog.io/@boorook/Python-%EB%B0%B1%EC%A4%80-2696-%EC%A4%91%EC%95%99%EA%B0%92-%EA%B5%AC%ED%95%98%EA%B8%B0-%EB%AC%B8%EC%A0%9C-%ED%92%80%EC%9D%B4
https://ahntoday.tistory.com/176 << 설명 개
/*
방식 1. 하나씩 읽어들어와 sort하여 값 추출
*/

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = null;
        int T = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < T; i++) {
            int N = Integer.parseInt(br.readLine()); // 배열의 크기
            sb.append(((N + 1) / 2)).append("\n"); // 중앙값의 개수 출력
            ArrayList<Integer> result = new ArrayList<>();
            for (int j = 0; j < N; j++) {
                if (j % 10 == 0) {
                    st = new StringTokenizer(br.readLine());
                }
                int x = Integer.parseInt(st.nextToken());
                result.add(x);
                Collections.sort(result);
                if (j % 2 == 0) {
                    if (result.size() % 10 == 9 || j == N - 1) {
                        sb.append(result.get(j / 2)).append("\n");
                    } else {
                        sb.append(result.get(j / 2)).append(" ");
                    }
                }
            }
        }
        bw.write(sb.toString());
        bw.flush();
        bw.close();
        br.close();
        
    }

}



/*
방식2
    *  min max를 활용하여 푸는데 키는 이것이다.
    *  max 즉 왼쪽에는 일정 수 이하의 값이 나열되게 해놓고
    *  min 즉 오른쪽에는 일정수 이상의 값이 나열되게 해놓는다.
    *  이렇게되면 max에는 3 2 1 min에는 4 5 가 되면서
    *  교환 하는 방식(max > min 이라면 교환)을 통해 계속 지속적으로 max에 min보다 작은 값들이 들어가게 되고 결국 max 제일 첫번째 값은 중앙 값이 되는 것
    *  max와 min을 아래와 같이 이어주는 것이라고 생각하면 편할거 같다.
    *  min
    *  5
    *  4
    *
    *  3
    *  2
    *  1
    *  max
    *  시간적 메모리적으로 거의 3배정도 차이난다 방식1
    * */

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = null;
        int T = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < T; i++) {
            PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Comparator.reverseOrder());
            PriorityQueue<Integer> minHeap = new PriorityQueue<>();
            int N = Integer.parseInt(br.readLine()); // 배열의 크기
            sb.append(((N + 1) / 2)).append("\n"); // 중앙값의 개수 출력
            for (int j = 0; j < N; j++) {
                if (j % 10 == 0) {
                    st = new StringTokenizer(br.readLine());
                }
                int x = Integer.parseInt(st.nextToken());
                // 입력받는 값들을 하나씩 차례대로 왼쪽, 오른쪽에 넣는 느낌.
                if (maxHeap.size() == minHeap.size()) {
                    maxHeap.offer(x);
                } else {
                    minHeap.offer(x);
                }

                // maxHeap은 중앙값 이하의 숫자만 갖도록 조정.
                if (!minHeap.isEmpty()) {
                    if (maxHeap.peek() > minHeap.peek()) {
                        int t1 = maxHeap.poll();
                        int t2 = minHeap.poll();

                        maxHeap.offer(t2);
                        minHeap.offer(t1);
                    }
                }
                if (j % 2 == 0) {
                    if ((maxHeap.size() + minHeap.size()) % 10 == 9 || j == N - 1) {
                        sb.append(maxHeap.peek()).append("\n");
                    } else {
                        sb.append(maxHeap.peek()).append(" ");
                    }
                }
            }
        }
        bw.write(sb.toString());
        bw.flush();
        bw.close();
        br.close();

    }

}

3번쨰 방식
이방식은 특정 값을 기준으로 작은 값을 small 큰 값을 big으로 넣으면서 해결하는 방식이다.
    


# -*- coding: utf8 -*- https://ahntoday.tistory.com/176
from sys import stdin
import heapq
# small은 최대힙 big은 최소힙으로 구성
# small에서 하나 뺀 거와 big에서 하나 뺀 거, 입력값1개 총 3개 중 중앙값을 구함.


def solution(data):
    smallh = []
    bigh = []
    middle = data[0]
    result = [middle]
    for idx, val in enumerate(data[1:], 1):
        if val > middle: # 1. middle값을 기준으로 왼쪽 오른쪽에 넣는다
            heapq.heappush(bigh, val)
        else:
            heapq.heappush(smallh, (-val, val))

        if idx % 2 == 0: # 2. middle 값을 기준으로 넣었을때 
            if len(smallh) < len(bigh): # big의 길이가 더길다면 middle을 small에 넣는다 그리고 big의 첫번쨰 값이 middle이 된다. 예를들어 middle이 1이고 2 3이 big에 들어가있다 생각하면된다.
                heapq.heappush(smallh, (-middle, middle))
                middle = heapq.heappop(bigh)
            elif len(smallh) > len(bigh): # small은 big과 같다. 이문제에서 핵심은 middle을 적절하게 설정하는 것인데 길이가 더 긴것중에 첫번쨰 값이 middle이 된다는것이 중요하다. 
                heapq.heappush(bigh, middle)
                middle = heapq.heappop(smallh)[1]
            result.append(middle)
    print(len(result))

    for i in range(len(result)):
        if i != 0 and (i+1) % 10 == 1:
            print()
        print(result[i], end=' ')
    print()


t = int(stdin.readline().rstrip())  # 테스트 케이스 개수
for i in range(t):
    m = int(stdin.readline().rstrip())  # 수열의 크기
    data = []
    if m % 10 == 0:
        for _ in range(m//10):
            data.extend(list(map(int, stdin.readline().rstrip().split(' '))))
    else:
        for _ in range(m//10+1):
            data.extend(list(map(int, stdin.readline().rstrip().split(' '))))

    solution(data)


