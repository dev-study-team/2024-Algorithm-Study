import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {

    /*
    문제풀이방법
    root 노드부터 갈 수 있는 경로를 모두 구해 max를 구하는 방식이었다.
    1. 실수 max 값을 초기화 한 실수
    2. visited에 방문했다 표시해야했는데 방문 순차를이상하게 해서 계속 틀리게 나왔다..

     */
    static int max = 0;
    static boolean[] visited;
    static List<Node>[] trees;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        trees = new ArrayList[N + 1];
        for (int i = 1; i <= N; i++) {
            trees[i] = new ArrayList<>();
        }

        for (int i = 0; i < N - 1; i++) {
            st = new StringTokenizer(br.readLine());
            int root = Integer.parseInt(st.nextToken());
            int leaf = Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());
            trees[root].add(new Node(leaf, weight));
            trees[leaf].add(new Node(root, weight));
        }

        for (int i = 1; i <= N; i++) {
            visited = new boolean[N + 1];
            visited[i] = true;
            List<Node> nodes = trees[i];
            for (Node node : nodes) { 
                //visited[node.to] = true;// nodes 가 한개있을경우 대비하여 먼저
                dfs(node.to, node.weight);
            }
        }
        System.out.println(max);
    }
    public static void dfs(int root,int sum) {
        List<Node> nodes = trees[root];
        visited[root] = true;

        if(nodes.size() == 1) {
            max = Math.max(max, sum);
            return;
        }
        for (Node node : nodes) {
            if(!visited[node.to]) {// nodes 가 한개있을경우 대비하여 먼저
                dfs(node.to, sum + node.weight);
            }
        }
    }

    static class Node {

        private int to;
        private int weight;

        public Node(int to, int weight) {
            this.to = to;
            this.weight = weight;
        }

        public int getTo() {
            return to;
        }

        public int getWeight() {
            return weight;
        }
    }

}

---
다른 사람 풀이

내가 걱정 했던 문제가 간선이 한개 남았을때면 더이상 갈 곳이 없으니 처리안할려했는데 for문에서 값이 없으면 안되니 그냥 아래와 같이 처리해도 되더라..

public class bj1967_트리의지름 {
	static int N;
	static class Node{
		int num, len;
		public Node(int num, int len) {
			this.num = num;
			this.len = len;
		}
	}
	static List<Node> list[];
	static boolean visit[];
	static int ans;
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(in.readLine());
		list = new ArrayList[N+1];
		for (int i = 1; i < N+1; i++) {
			list[i] = new ArrayList<Node>();
		}
		for (int i = 0; i < N-1; i++) {
			StringTokenizer st = new StringTokenizer(in.readLine());
			int from = Integer.parseInt(st.nextToken());
			int to = Integer.parseInt(st.nextToken());
			int len = Integer.parseInt(st.nextToken());
			list[from].add(new Node(to, len));
			list[to].add(new Node(from, len));
		}
		ans = 0;
		for (int i = 1; i <= N; i++) {
			visit = new boolean[N+1];
			visit[i] = true;
			dfs(i, 0);
		}
		System.out.println(ans);
	}
	private static void dfs(int num, int dim) {
		for (Node node : list[num]) {
			if(!visit[node.num]) {
				visit[node.num] = true;
				dfs(node.num, dim + node.len);
			}
		}
		ans = (ans < dim)? dim : ans;
	}
}

---

다른 사람풀이
dfs로 루트 1을 놨두고 1에서 내려갈때 제일 큰 가중치를 가진 선을 한개를 찾는다. 선에 마지막 노드를 구하고 노드부터 경로를 다시 위로 올라가면
해결되는 문제였다.
아마도 루트는 모든 경로를 다 거치니 이걸 이용해서 구현하는거 같다.


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main {
    static ArrayList<Node>list[] ;
    static int n;
    static int max = 0;
    static boolean visited[];
    static int max_idx = 0;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        
        n = Integer.parseInt(br.readLine());
        
        
        list = new ArrayList[n+1];
        
        for(int i=0; i<=n; i++) {
            list[i] = new ArrayList<>();
        }
        
        
        
        
        for(int i=0; i<n-1; i++) {
            String [] t = br.readLine().split(" ");
            int parent = Integer.parseInt(t[0]);
            int child = Integer.parseInt(t[1]);
            int weight = Integer.parseInt(t[2]);
            list[parent].add(new Node(child,weight));
            list[child].add(new Node(parent,weight));
        }
        
        visited = new boolean[n+1];
        visited[1] = true;
        dfs(1,0);
        
        
        visited = new boolean[n+1];
        visited[max_idx] = true;
        dfs(max_idx,0);
        System.out.println(max);
        
    }
    public static void dfs(int idx, int cnt) {
        
        if(max < cnt) {
            max = cnt;
            max_idx = idx;
        }
        
        
        
        for(Node a : list[idx]) {
            if(!visited[a.idx]) {
                visited[a.idx] = true;
                dfs(a.idx, cnt+a.cnt);
            }
        }
    }
}
class Node{
    int idx,cnt;
    Node(int idx, int cnt){
        this.idx = idx;
        this.cnt = cnt;
    }
}  

