# import sys
# from bisect import bisect_left, bisect_right

# # n - 집의 개수, c - 공유기 개수
# n,c = map(int,sys.stdin.readline().split())
# house=list()
# for i in range(n):
#   house.append(int(sys.stdin.readline()))

# house.sort()

# # 반 가르고 구역을
# target=(house[0]+house[len(house)-1])//2

# # 가장 반갈이랑 가까운 집
# close_mid=-1
# mid=bisect_left(house,target)
# if abs(target-house[mid])>abs(target-house[mid-1]):
#   close_mid=mid-1
# else:
#   close_mid=mid

# print(house[close_mid])

# count=2
# array=list()
# array.append(house[0])
# array.append(house[len(house)-1])

# if c<2:
#   print(house[len(house)-1]-house[0])
# else:
#   start=0
#   end=len(house)-1
#   while count!=c:
#     mid=bisect_left(house,target,start,end)
#     if abs(target-house[mid])>abs(target-house[mid-1]):
#       array.append(house[mid-1])
#       start=mid
#     else:
#       array.append(house[mid])
#       end=mid-1
#     target