import time

start=time.time()

n, m = map(int,input().split())

result=0
for i in range(n):
  l=list(map(int,input().split()))
  min_num=min(l)
  if result<min_num:
    result=min_num

print(result)

end=time.time()
print("time :", end - start) # 수행 시간 출력