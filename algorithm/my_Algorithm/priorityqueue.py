import heapq # 힙 자료구조 사용을 위한 import
from queue import PriorityQueue # 우선순위 큐 자료구조

# 힙 생성
heap = []

# 데이터 삽입
data=1
heapq.heappush(heap,data)

# 데이터 삭제
one = heapq.heappop(heap)

# 우선순위 큐 생성
q=PriorityQueue()

# 데이터 삽입
q.put(1)

# 데이터 삭제
num1=q.get()

# 우선순위 큐 사이즈 확인
length=q.qsize()
q.empty() # true or false