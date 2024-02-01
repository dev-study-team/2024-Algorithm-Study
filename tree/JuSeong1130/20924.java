package tree;

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

public class b20924 {

    /*
    실수한것
    1. gigaroot가 설정되지 않아 null이 나올 수 있는데 이를 간과함
    
    고려해야했던것
    1. 기둥만 있는것
    2. 기둥은 없고 나뭇가지만 있는것
    3. 기둥 나뭇가지가 있는것

    1,2번을 고려하지 못해 1번은 실수한것에서 null 에러로 나오게 되었고 2번은 잘못된 값을 유도하게 했다.
    아래 값을 입력했을때 7 0 이나오게됬다. 0 4 가나와야 하는데 말이다.
    이유는 1 2 가 연결되어있다면 1에 2 그리고 2에 1이 입력되어있는데 내가 한것은 부모가 있는 것을 기준으로 만했다.
    리프노드를 확인하기 위한 식은 leafs.size > 2 였는데 부모노드간선 한개와 밑에 간선한개 즉 2개였다.
    그런데 부모노드는 부모 간선이 없으므로 leafs.size > 1이 되야했다.
3 2
1 2 3
2 3 4

     */
    static int branch = 0;
    static boolean[] visited;
    static Map<Integer, ArrayList<Node>> map;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int R = Integer.parseInt(st.nextToken());

        map = new HashMap<>();
        for (int i = 1; i <= N; i++) {
            map.put(i,new ArrayList<>());
        }

        for (int i = 0; i < N - 1; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int d = Integer.parseInt(st.nextToken());
            map.get(a).add(new Node(b,d));
            map.get(b).add(new Node(a,d));
        }
        visited = new boolean[N+1];
        Queue<Integer> queue = new LinkedList<>();
        queue.add(R);
        visited[R] = true;

        int pillar = 0;
        int gigaRoot = -1;
        while (!queue.isEmpty()) {
            Integer num = queue.poll();
            List<Node> leafs = map.get(num);
            int size = R == num ? 1 : 2;
            if (leafs.size() > size) {
                gigaRoot = num;
                break;
            }
            for (Node node : leafs) {
                int leaf = node.getLeaf();
                if (!visited[leaf]) {
                    visited[leaf] = true;
                    pillar += node.getWeight();
                    queue.add(leaf);
                }
            }
        }
        dfs(gigaRoot, 0);
        System.out.println(pillar + " " + branch);

    }
    public static void dfs(int root, int sum) {
        if(root == -1) {
            return;
        }
        visited[root] = true;
        List<Node> nodes = map.get(root);
        if (nodes.size() == 1) {
            branch = Math.max(sum, branch);
            return;
        }
        for (Node node : nodes) {
            int leaf = node.getLeaf();
            if(!visited[leaf]) {
                dfs(node.getLeaf(), sum + node.getWeight());
            }
        }
    }

    static class Node {
        private int leaf;
        private int weight;

        public Node(int leaf, int weight) {
            this.leaf = leaf;
            this.weight = weight;
        }

        public int getLeaf() {
            return leaf;
        }

        public int getWeight() {
            return weight;
        }
    }

}


---다른 사람풀이

static ArrayList<int[]>[] children;
    static boolean[] vtd;
    static int branch;
    static int trunk;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        trunk = 0;
        branch = 0;
        int N = Integer.parseInt(st.nextToken());
        int R = Integer.parseInt(st.nextToken());
        vtd = new boolean[N + 1];
        children = new ArrayList[N + 1];
        for (int n = 1; n <= N; n++) children[n] = new ArrayList<>();
        for (int n = 1; n < N; n++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int d = Integer.parseInt(st.nextToken());
            children[a].add(new int[]{b, d});
            children[b].add(new int[]{a, d});

        }
        vtd[R] = true;
        if (children[R].size() == 1) {
            vtd[children[R].get(0)[0]] = true;  //root를 먼저 해서 size 1의 처리를 먼저해줌
            trunk += children[R].get(0)[1];
            findBranch(findTrunk(children[R].get(0)[0]), 0);
        } else findBranch(R, 0);
        System.out.println(trunk + " " + branch);
    }

    static int findTrunk(int root) {
        while (children[root].size() == 2) {
            for (int[] child : children[root]) {
                if (!vtd[child[0]]) {
                    vtd[child[0]] = true;
                    trunk += child[1];
                    root = child[0];
                }
            }
        }
        return root;
    }

    static void findBranch(int node, int length) {
        if (children[node].size() == 1) branch = Math.max(branch, length);
        for (int[] child : children[node]) {
            if (!vtd[child[0]]) {
                vtd[child[0]] = true;
                findBranch(child[0], child[1] + length);
                vtd[child[0]] = false;
            }
        }
    }
    
