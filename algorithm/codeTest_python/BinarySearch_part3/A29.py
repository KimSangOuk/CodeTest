import sys

# n - 집의 개수, c - 공유기 개수
n,c = map(int,sys.stdin.readline().split())
house=list()
for i in range(n):
  house.append(int(sys.stdin.readline()))

house.sort()