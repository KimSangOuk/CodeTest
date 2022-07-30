import sys

def binary_search(array,target,start,end):
  while start<=end:
    mid = (start+end)//2
    if array[mid]==target:
      return mid
    elif array[mid]>target:
      end=mid-1
    else:
      start=mid+1
  return None

# 가게의 부품 총 n개
n = int(sys.stdin.readline().rstrip())
# 가게의 총 부품 번호 배열
array = list(map(int,sys.stdin.readline().split()))

# 이진 탐색을 위해 정렬
# array.sort()

# 찾아야 하는 부품 개수, m
m = int(sys.stdin.readline().rstrip())
# 찾아야 하는 부품의 배열, array1
array1=list(map(int,sys.stdin.readline().split()))

# 찾아야 하는 부품도 정렬
array1.sort()

for i in array1:
  if binary_search(array,i,0,n-1)==None:
    print("no",end=' ')
  else:
    print("yes",end=' ')