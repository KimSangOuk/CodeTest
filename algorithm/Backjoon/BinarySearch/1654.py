import sys

def binary_search(array,target,start,end):
  while start<=end:
    mid=(start+end)//2
    sum=0
    # 랜선을 나누었을 때 총 갯수
    for i in array:
      if i!=0:
        sum+=i//mid
    # 나눈 랜선의 갯수가 목표 갯수보다 작으면 더 작은 단위로 나누기 위해 줄임
    if sum<target:
      end=mid-1
    # 나눈 랜선의 갯수가 목표 갯수보다 크거나 같으면 찾은거기 때문에 최댓값을 찾기 위해 더 나눠서 찾음
    else:
      result=mid
      start=mid+1
  return result

# 현재 가지고 있는 랜선의 갯수 k, 필요한 랜선의 갯수 n
k,n=map(int,sys.stdin.readline().split())

# 현재 가지고 있는 랜선의 길이 배열
array=list()
for i in range(k):
  array.append(int(sys.stdin.readline()))

# 길이는 1에서부터 가장 큰 array까지 - 원래가지고 있는 랜선들보다 길어도 되기 때문
result=binary_search(array,n,1,max(array))

print(result)