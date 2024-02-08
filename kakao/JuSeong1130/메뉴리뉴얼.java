## 내 생각, 어려웠던점

문제에서 조합을 이용해서 구하라 해서 당연스럽게 조합을 사용했다.

또한 해당 글자열 길이에 최대 카운트 개수의 문자열을 구해야 해서 int[] 배열을 이용해 해당 글자열의 최대 카운트 개수를 구하고 이를 이용해서 답을 구현해 내었다.

어려웠던점

일단 첫번째로 문자열을 정렬하고 시작해야 했다 조건이 너무 많다.

두번쨰로 조합이 익숙치 않았다.

세번째 어떻게 맥스값을 저장해놓고 이용할 수 있을까가 어려웠다.

## 코드

```jsx
import java.util.*;
import java.util.stream.*;
/*
단품을 조합해서 코스요리로 , 가장 많이 함께 주문한 단품메뉴를 코스요리로
코스요리 2가지 이상 단품 메뉴로 구성하려고함 단 손님이 2명이상 주문한거만 후보로

조합으로 하면될듯

*/

class Solution {
    Map<String,Integer> courses = new HashMap<>();
    int[] max = new int[21];
    public String[] solution(String[] orders, int[] course) {
        
        List<String> ordersSort = new ArrayList<>();
        for (String s : orders) {
            ordersSort.add(
                s.chars()
                .sorted()
                .mapToObj(c -> String.valueOf((char)c))
                .collect(Collectors.joining())
            );
        }
  
        
        
        for (int i = 0; i < course.length; i++) {
            int count = course[i];
            for(int j = 0; j < ordersSort.size(); j++) {
                if(ordersSort.get(j).length() >= count) {
                    combinations(ordersSort.get(j), 0, count, "");
                }
            }
        }
        List<String> result = new ArrayList<>();
        for (String key : courses.keySet()) {
             if(courses.get(key) > 1 && max[key.length()] == courses.get(key)) {
                 result.add(key);
             }   
        }
        Collections.sort(result);
        String[] answer = new String[result.size()];
        for (int i = 0; i < result.size(); i++) {
            answer[i] = result.get(i);
        }
        return answer;
    }
    public void combinations(String order,int index, int count, String str) {
        
        if(str.length() == count) {
            courses.put(str, courses.getOrDefault(str, 0) + 1);
            max[count] = Math.max(max[count], courses.get(str));
            return;
        }
        
        for (int i = index; i < order.length(); i++) {
            combinations(order, i + 1, count, str + order.charAt(i));
        }
    }
    
    
    
    
}

```

## 다른 사람 생각, 코드

https://jisunshine.tistory.com/146

https://coding-grandpa.tistory.com/102

나는 글자열 길이와 상관없이 그냥 모두 map에넣고 한번에 해결하는데

다른 사람들은 글자열 길이마다 map을 초기화 시켜 이를 이용하는 방식으로 구현 하였다.


```
  import java.util.*;

class Solution {

    List<String> answerList = new ArrayList<>();
    Map<String, Integer> hashMap = new HashMap<>();

    public String[] solution(String[] orders, int[] course) {

        // 1. 각 Order 정렬
        for (int i = 0; i < orders.length; i++) {
            char[] arr = orders[i].toCharArray();
            Arrays.sort(arr);
            orders[i] = String.valueOf(arr);
        }

        // 2. 각 order를 기준으로 courseLength 만큼의 조합 만들기
        for (int courseLength : course) {
            for (String order : orders)
                combination("", order, courseLength);

            // 3. 가장 많은 조합 answer에 저장
            if (!hashMap.isEmpty()) {
                List<Integer> countList = new ArrayList<>(hashMap.values());
                int max = Collections.max(countList);

                if (max > 1)
                    for (String key : hashMap.keySet())
                        if (hashMap.get(key) == max)
                            answerList.add(key);
                hashMap.clear();
            }
        }

        Collections.sort(answerList);
        String[] answer = new String[answerList.size()];
        for (int i = 0; i < answer.length; i++)
            answer[i] = answerList.get(i);

        return answer;
    }

    public void combination(String order, String others, int count) {
        // 탈출 조건 : count == 0
        if (count == 0) {
            hashMap.put(order, hashMap.getOrDefault(order, 0) + 1);
            return;
        }

        // 0부터 length까지 조합
        for (int i = 0; i < others.length(); i++)
            combination(order + others.charAt(i), others.substring(i + 1), count - 1);
    }
    public static void main(String[] args){
        Solution sol = new Solution();
        String[] orders = {"ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"};
        int[] course = {2,3,4};
        System.out.println(sol.solution(orders, course));
    }
}
```
  
