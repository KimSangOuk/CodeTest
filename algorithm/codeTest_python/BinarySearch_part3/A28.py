import sys

def find_fixed_point(array,start,end):
  while start<=end:
    mid=(start+end)//2
    if array[mid]==mid:
      return mid
    elif array[mid]<mid:
      start=mid+1
    else:
      end=mid-1
  return None

n = int(sys.stdin.readline())
array=list(map(int,sys.stdin.readline().split()))

result=find_fixed_point(array,0,len(array)-1)
if result==None:
  print(-1)
else:
  print(result)