

내풀이 시간 초과

1. 노드를 삭제하고
2. 그래프의 개수를 큐를 이용해 bfs방식으로 구하고 
3. 개수에 따라 구하게 하였다.

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

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        Map<Integer, List<Integer>> map = new HashMap<>();
        for (int i = 1; i <= N; i++) {
            map.put(i, new ArrayList<>());
        }
        StringTokenizer st;
        for (int i = 0; i < N - 1; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            map.get(a).add(b);
            map.get(b).add(a);
        }
        int q = Integer.parseInt(br.readLine());
        boolean[] visited;
        for (int i = 0; i < q; i++) {
            st = new StringTokenizer(br.readLine());
            int t = Integer.parseInt(st.nextToken());
            int k = Integer.parseInt(st.nextToken());
            visited = new boolean[N+1];
            Queue<Integer> queue = new LinkedList<>();
            if (t == 1) { // k가 단절점인지
                visited[k] = true;
                int count = 0;
                for (int j = 1; j <= N; j++) {
                    if(!visited[j]) {
                        count++;
                        queue.add(j);
                        visited[j] = true;
                        while (!queue.isEmpty()) {
                            Integer poll = queue.poll();
                            List<Integer> integers = map.get(poll);
                            for (Integer integer : integers) {
                                if (!visited[integer]) {
                                    queue.add(integer);
                                    visited[integer] = true;
                                }
                            }
                        }
                    }
                }

                if (count < 2) {
                    System.out.println("no");
                } else  {
                    System.out.println("yes");
                }

            } else { // k가 단절선인지
                System.out.println("yes");
            }
        }
    }
}

---
  https://loosie.tistory.com/522
중요한건 그래프가 2개가 되냐 안되냐였다

간선은 자르면 무조건 그래프가 2개가 되니 무조건 yes다
노드는 간선의 개수가 2개이상이면 무조건 yes다 왜냐하면 부모노드 간선 1개 그리고 자식 노드 간선 1개가 있을때 그 노드를 자르면 그래프가 2개이상 나오기 때
  
map을 안쓰고 아래와 같은 방식으로도 구현 가능하다.
        list = new ArrayList[n + 1];
        for(int i = 1; i < n + 1; i++) {
            list[i] = new ArrayList<>();
        }
  
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		
		StringTokenizer st;
		List<Integer>[] list = new ArrayList[n+1];
		for(int i=1; i<n+1; i++) {
			list[i] = new ArrayList<>();
		}
		for(int i=0; i<n-1; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			list[a].add(b);
			list[b].add(a);
		}
		
		StringBuilder sb = new StringBuilder();
		int q = Integer.parseInt(br.readLine());
		for(int i=0; i<q; i++) {
			st = new StringTokenizer(br.readLine());
			int op = Integer.parseInt(st.nextToken());
			if(op==2) {
				sb.append("yes\n");
			}else {
				int idx = Integer.parseInt(st.nextToken());
				if(list[idx].size() >=2) sb.append("yes\n");
				else sb.append("no\n");
			}
		}
		System.out.println(sb.toString());
	}
}

  


