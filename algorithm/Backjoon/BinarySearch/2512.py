import sys

def binary_search(array,target,start,end):
  result=0
  while start<=end:
    mid = (start+end)//2
    # print(start,end)
    # print(mid)
    sum=0
    for i in array:
      if i<=mid:
        sum+=i
      else:
        sum+=mid
    # print(sum)
    
    if sum>target:
      end=mid-1
    elif sum<=target:
      result=mid
      start=mid+1
  return result

# 지방의 수 n
n = int(sys.stdin.readline())

# 각 지방의 예산 요청
array = list(map(int,sys.stdin.readline().split()))

# 총 예산 m
m = int(sys.stdin.readline())

print(binary_search(array,m,0,max(array)))