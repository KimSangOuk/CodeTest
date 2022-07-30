import sys

def get_rest(array,value):
  sum=0
  for i in array:
    if i-value<0:
      sum+=0
    else:
      sum+=(i-value)
  # print(sum)
  return sum

def binary_search(array,target,start,end):
  while start<=end:
    mid=(start+end)//2
    if get_rest(array,mid)==target:
      # print(mid)
      return mid
    elif get_rest(array,mid)>target:
      start=mid+1
    else:
      end=mid-1

# 떡의 개수 n, 요청한 떡의 길이 m
n, m = map(int,sys.stdin.readline().split())

# 떡의 개별 높이, array
array = list(map(int,sys.stdin.readline().split()))

result=binary_search(array,m,0,max(array))

print(result)