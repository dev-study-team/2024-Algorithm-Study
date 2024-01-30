
/*
문제풀이 방법 
root 노드는 1부터 시작한다. 
1의 자식들을 가져온다. 이때 자식노드의 부모노드를 1로 설정해놓고 큐에 자식노드를 넣는다.
이것을 반복하다보면 1에 자식A의 자식B의 부모는 자식A가 되게 된다. 
단. 중복되는 경우가 있을 수 있으니 visited에 값이 0 이아닐때를 구하면 되는 문제다.

*/


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
class Main{
   public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(in.readLine());
        List<Integer> list[] = new ArrayList[N+1];
        for (int i = 0; i < list.length; i++) {
            list[i] = new ArrayList<Integer>();
        }
        for (int i = 0; i < N-1; i++) {
            StringTokenizer st = new StringTokenizer(in.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            list[a].add(b);
            list[b].add(a);
        }
        boolean visit[] = new boolean[N+1];
        Queue<Integer> queue = new LinkedList<Integer>();
        queue.add(1);
        visit[1] = true;
        int ans[] = new int [N+1];
        //1이 부모니 1의 자식들을 찾아 넣기0
        while(!queue.isEmpty()){
            Integer num = queue.poll();
            for(Integer i : list[num]){
                if(!visit[i]){
                    ans[i]=num;
                    visit[i]=true;
                    queue.add(i);
                }
            }
        }
        for (int i = 2; i < ans.length; i++) {
            System.out.println(ans[i]);
        }
    }
}

---


아래는 위와 같은 생각이나 다른 자료구조로 구현한 것이다.

import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.Scanner;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        Map<Integer, List<Integer>> map = IntStream.rangeClosed(1, N)
                .boxed()
                .collect(Collectors.toMap(
                        key -> key,
                        value -> new ArrayList<>()
                ));
        for (int i = 0; i < N -1; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            map.get(x).add(y);
            map.get(y).add(x);
        }
        Queue<Integer> queue = new LinkedList<>();
        boolean[] visited = new boolean[N+1];
        queue.add(1);
        visited[1] = true;
        Map<Integer,Integer> result = new HashMap<>();
        while (!queue.isEmpty()) {
            int root = queue.poll();
            for(Integer num : map.get(root)) {
                if(!visited[num]) {
                    result.put(num,root);
                    visited[num] = true;
                    queue.add(num);
                }
            }
        }

        for (int i = 2; i <= N; i++) {
            System.out.println(result.get(i));
        }

    }

}
  
