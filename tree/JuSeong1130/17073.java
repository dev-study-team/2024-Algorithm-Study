https://www.acmicpc.net/problem/17073
https://loosie.tistory.com/523
다른사람풀이 핵심 리프노드는 간선1개만 존재하는게 리프노드임 그걸 이용
for(int i=2; i<n+1; i++) {
			if(list[i].size()==1) leafN++;
		}


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    /*
    문제 풀이 방법
    이 문제는 결국 맨 위 루트부터 균등하게 즉 2개라면 2분의 1씩 내려가게되는데 더이상 내려가지 못하면 멈추고
    그들의 평균값을 구하는 문제이다.
    즉 가지고있는 W만큼 물 / 리프노드의 수를 하면 결과가 나오게 된다.
     */

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int W = Integer.parseInt(st.nextToken());
        Map<Integer, List<Integer>> map = new HashMap<>();
        for (int i = 1; i <= N; i++) {
            map.put(i,new ArrayList<>());
        }

        for (int i = 0; i < N - 1; i++) {
            st = new StringTokenizer(br.readLine());
            int U = Integer.parseInt(st.nextToken());
            int V = Integer.parseInt(st.nextToken());
            map.get(U).add(V);
            map.get(V).add(U);
        }
        boolean[] visited = new boolean[N+1];
        int leafNode = 0;

        Queue<Integer> queue = new LinkedList<>();
        queue.add(1);
        visited[1] = true;
        while (!queue.isEmpty()) {
            Integer num = queue.poll();
            List<Integer> leafs = map.get(num);
            int count = 0;
            for (int i = 0; i < leafs.size(); i++) {
                Integer leaf = leafs.get(i);
                if(!visited[leaf]) {
                    queue.add(leaf);
                    visited[leaf] = true;
                    count++;
                }
            }

            if (count == 0) {
                leafNode++;
            }
        }
        
        System.out.printf("%.10f%n", (double)W/leafNode);
    }
}
