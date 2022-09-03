import sys

def binary_search(x,y,target,start,end):
  result=0
  while start<=end:
    mid=(start+end)//2
    tmp_x=x+mid
    tmp_y=y+mid
    tmp_z=int(tmp_y*100/tmp_x)
    # print(target, tmp_z)
    if tmp_z>target:
      result=mid
      end=mid-1
    else:
      start=mid+1
  if result==0:
    return -1
  return result

# x - 게임 횟수, y - 이긴 게임 수
x, y = map(int,sys.stdin.readline().split())

# z - 승률
z = int(y*100/x)


print(binary_search(x,y,z,0,x))