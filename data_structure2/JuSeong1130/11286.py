

"""
만약 x가 0이 아니라면 배열에 x라는 값을 넣는(추가하는) 연산이고, x가 0이라면 배열에서 절댓값이 가장 작은 값을 출력하고 그 값을 배열에서 제거하는 경우이다. 


"""
import heapq,sys

N = int(sys.stdin.readline())

heap = []

for i in range(N) :
    x = int(sys.stdin.readline())
    if x == 0 :
        if heap :
            print(heapq.heappop(heap)[1])
        else :
            print(0)
    else : 
        heapq.heappush(heap, (abs(x), x)) # 절대값과 원래 값을 넣어야 하는 문제였다.

자바에서는 아래와 같이 구현한다.
절대 값이 같다면 원래 있던 값을 기준으로 하면되고
다르다면 절대값을 기준으로 우선순위를 해주면된다.

BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		PriorityQueue<Integer> pq = new PriorityQueue<Integer>(new Comparator<Integer>() {
			@Override
			public int compare(Integer o1, Integer o2) {
				//절대값 기준으로 앞 값이 더 크다면 자리를 바꿔준다.
				if(Math.abs(o1) > Math.abs(o2)) {
					return Math.abs(o1) - Math.abs(o2);
				//절대값 기준으로 두 값이 같다면 음수를 앞으로 보내준다.
				}else if(Math.abs(o1) == Math.abs(o2)) {
					return o1 - o2;
				}else {
					return -1;
				}
			}
		});
		StringBuilder sb = new StringBuilder();
		
		for(int i = 0; i < N; i++) {
			int x = Integer.parseInt(br.readLine());
			if(x == 0) {
				if(pq.isEmpty()) sb.append("0").append("\n");
				else sb.append(pq.poll()).append("\n");
			}else {
				pq.offer(x);
			}
		}
		System.out.println(sb);
	}
