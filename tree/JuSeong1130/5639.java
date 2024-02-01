


package tree;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class b5639 {

    static class Node {

        private int num;
        private Node left;
        private Node right;

        public Node(int num) {
            this.num = num;
        }

        public void insert(int inputNum) {
            if(num > inputNum) {
                if(left == null) {
                    left = new Node(inputNum);
                } else {
                    left.insert(inputNum);
                }
            } else {
                if(right == null) {
                    right = new Node(inputNum);
                } else {
                    right.insert(inputNum);
                }
            }
        }

        public int getNum() {
            return num;
        }

        public Node getLeft() {
            return left;
        }

        public Node getRight() {
            return right;
        }
    }
    /*
    문제풀이 방법
    루트왼쪽은 작은거 오른쪽은 큰거이니 루트보다 큰게 나오기전까지
    왼쪽으로 계속 넣는다 그리고 큰게 나오면 오른쪽으로 넣고 트리를 완성한 이후에
    트리가지고 후위진행으로 값을 구해내면 된다.

    트리를 만드는 방법을 맨처음에 while을 이용해 root node와 current node? 두개의 변수를 가지고 진행하려했는데 이렇게 하면 dfs를 이용해야할거같다.
    그래서 그냥 node class에 집어넣어 dfs하는 방식으로 하였다.( 답 찾아봄)

    
     */

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        Node root = new Node(Integer.parseInt(br.readLine()));
        String input;
        while (true) {
            input = br.readLine();
            if (input == null || input.equals(""))
                break;
            root.insert(Integer.parseInt(input));
        }
        postOrder(root);

    }

    //후위 순회 (왼쪽-오른쪽-루트)
    public static void postOrder(Node node) {
        if(node == null) {
            return;
        }
        postOrder(node.getLeft());
        postOrder(node.getRight());
        System.out.println(node.getNum());
    }




}
