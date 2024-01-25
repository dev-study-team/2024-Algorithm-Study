

/*
내 생각 
노드에 들어오는 선이 2개이상이라면 tree가 아니라고 생각했으나 root도 한개여야 했던 문제였다.

다른사람의 풀이를 보다보니 map에 u와 v 둘다 넣어주고 u는 0으로 유지시키는 방식을 통해 root를 판단할 수 있게 해주었다.

*/


import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;


public class Main {

    public static void main(String[] args)  {
        Scanner sc = new Scanner(System.in);

        Map<Integer, Integer> map = new HashMap<>();
        int k = 1;
        while (true) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            if (u < 0 && v < 0) {
                break;
            }
            if (u == 0) {
                if(map.isEmpty()) {
                    System.out.println("Case " + k + " is a tree.");
                } else {
                    int rootCount = 0;
                    boolean isTree = true;
                    for(Integer key : map.keySet()) {
                        if(map.get(key) == 0) {
                            rootCount++;
                        }
                        if(map.get(key) > 1) {
                            isTree = false;
                        }
                    }

                    if(rootCount == 1 && isTree) {
                        System.out.println("Case " + k + " is a tree.");
                    } else {
                        System.out.println("Case " + k + " is not a tree.");
                    }
                }
                k++;
                map = new HashMap<>();
                continue;
            }
            map.put(u, map.getOrDefault(u, 0)); // u 노드 있으니 0 만약 0 이 유지되면 루트노드
            map.put(v, map.getOrDefault(v, 0) + 1); //v로 들어오는 선 있으니 +1
        }
    }

}
