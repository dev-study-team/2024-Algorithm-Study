https://usedto-wonderwhy.tistory.com/175 나랑 비슷한 풀이 dfs이

https://moonsbeen.tistory.com/229 다른 풀이
방법
1. parent[] 배열을 놨두고 자기의 부모를 설정한다.
2. 삭제된 노드를 부모로가지고 있는 것들을 parent[?] = -2를 통해 삭제처리된거 처럼 한다.
3. countLeaf라는 dfs 방식 메서드를 통해 count를 구한다.


import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.Stack;

public class Main {

    /*
    *
    map에는 자식노드
    roots에는 부모노드를 넣는다

    removeNode를 입력받았을때 그 노드의 부모노드를 찾아 부모노드의 자식노드 list를꺼내 removeNode에 대해서 삭제해준다.
    그러면 삭제가되므로 더이상연결되지 않으니 문제에서 구하는 답을 구할 수 있다.

    
    *
    * */
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        Map<Integer, List<Integer>> map = new HashMap<>();
        int[] roots = new int[N];

        for (int i = 0; i < N; i++) {
            map.put(i, new ArrayList<>());
        }

        int root = 0;
        for (int i = 0; i < N; i++) {
            int parent = sc.nextInt();
            if (parent == -1) {
                root = i;
            } else {
                map.get(parent).add(i);
            }
            roots[i] = parent;
        }

        int removeNode = sc.nextInt();
        int result = 0;
        if(removeNode != root) {
            map.get(roots[removeNode]).remove(Integer.valueOf(removeNode));
            Stack<Integer> stack = new Stack<>();
            stack.add(root);
            while (!stack.isEmpty()) {
                int node = stack.pop();
                List<Integer> nodes = map.get(node);
                if(nodes.isEmpty()) {
                    result++;
                } else {
                    for (Integer integer : nodes) {
                        stack.push(integer);
                    }
                }
            }
        }
        System.out.println(result);
    }

}
