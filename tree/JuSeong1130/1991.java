
문제풀이방법
Node에 leftNode와 rightNode를 집어 넣어놓고 
재귀나 stack을 이용해 순회의 순서에 맞게 값을 넣어주면되는 문제다.
재귀에 대해 다시 공부해 봐야겠다..
재귀 귀납법.. A(1)이 됬을때 A(N)이 된다면 A(N-1)도 ..?

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;
import java.util.Queue;
import java.util.Scanner;
import java.util.Stack;

public class Main {
    static Map<String,Node> map;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        map = new HashMap<>();
        char c = 'A';
        for (char i = 'A'; i < c+N; i++) {
            map.put(String.valueOf(i),new Node(String.valueOf(i)));
        }
        for (int i = 0; i < N; i++) {
            String[] s = br.readLine().split(" ");
            Node rootNode = map.get(s[0]);
            Node leftNode = map.get(s[1]);
            Node rightNode = map.get(s[2]);
            if(leftNode == null) {
                leftNode = new Node(".");
            }
            if (rightNode == null) {
                rightNode = new Node(".");
            }
            rootNode.setLeft(leftNode);
            rootNode.setRight(rightNode);
        }
        System.out.println(preOrder("A"));
        System.out.println(inOrder(map.get("A")));
        System.out.println(postOrder(map.get("A")));

    }
    // root 무조건 먼저하고 그다음에 왼쪽 그다음에 오른쪽
    public static String preOrder(String root) {
        Stack<Node> stack = new Stack<>();
        StringBuilder sb = new StringBuilder();
        stack.push(map.get(root));
        while (!stack.isEmpty()) {
            Node n = stack.pop();
            sb.append(n.getData());
            if(!n.getRight().getData().equals(".")){
                stack.add(n.getRight());
            }
            if(!n.getLeft().getData().equals(".")){
                stack.add(n.getLeft());
            }
        }
        return sb.toString();
    }
    //(왼쪽 자식) (루트) (오른쪽 자식)
    public static String inOrder(Node root) {
        String answer = "";
        if(root.getData().equals(".")){
            return "";
        }
        answer += inOrder(root.getLeft());
        answer += root.getData();
        answer += inOrder(root.getRight());
        return answer;
    }

    //(왼쪽 자식) (오른쪽 자식) (루트)
    public static String postOrder(Node root) {
        String answer = "";
        if(root.getData().equals(".")){
            return "";
        }
        answer += postOrder(root.getLeft());
        answer += postOrder(root.getRight());
        answer += root.getData();
        return answer;
    }
    
    static class Node {
        String data;
        Node left;
        Node right;

        public Node(String data) {
            this.data = data;
        }

        public void setLeft(Node left) {
            this.left = left;
        }

        public void setRight(Node right) {
            this.right = right;
        }

        public String getData() {
            return data;
        }

        public Node getLeft() {
            return left;
        }

        public Node getRight() {
            return right;
        }
    }


}

