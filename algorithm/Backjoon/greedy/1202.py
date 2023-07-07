import sys
import heapq
input=sys.stdin.readline

q=[]

n,k=map(int,input().split())

for _ in range(n):
  m,v=map(int,input().split())
  heapq.heappush(q,(m,-v))




    