import sys

def binary_search(array,target,start,end):
  while start<=end:
    mid = (start+end)//2
    if array[mid]==target:
      return 1
    elif array[mid]<target:
      start=mid+1
    else:
      end=mid-1
  return 0

t = int(sys.stdin.readline())

for i in range(t):
  n = int(sys.stdin.readline())
  array1=list(map(int,sys.stdin.readline().split()))
  m = int(sys.stdin.readline())
  array2=list(map(int,sys.stdin.readline().split()))
  array1.sort()
  for j in array2:
    print(binary_search(array1,j,0,len(array1)-1))