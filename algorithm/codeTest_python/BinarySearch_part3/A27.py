import sys

def find_first(array,target,start,end):
  while start<=end:
    mid=(start+end)//2
    if array[mid]==target and (mid-1>=0 or mid==0) and array[mid-1]<target:
      return mid
    elif array[mid]>=target:
      end=mid-1
    else:
      start=mid+1
  return None

def find_last(array,target,start,end):
  while start<=end:
    mid=(start+end)//2
    if array[mid]==target and (mid+1<=len(array)-1 or mid==len(array)-1) and array[mid+1]>target:
      return mid
    elif array[mid]<=target:
      start=mid+1
    else:
      end=mid-1
  return None

# 숫자의 갯수 n, 갯수를 알아야하는 숫자 x
n, x = map(int,sys.stdin.readline().split())

# 배열
array = list(map(int,sys.stdin.readline().split()))

first=find_first(array,x,0,len(array)-1)
last=find_last(array,x,0,len(array)-1)

if first==None and last==None:
  print(-1)
else:
  print(last)
  print(first)
  print(last-first+1)