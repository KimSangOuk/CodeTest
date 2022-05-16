import time

start=time.time()

n,m,k=map(int,input().split())
data=list(map(int,input().split()))

data.sort()

print(m*data[n-1]-(data[n-1]-data[n-2])*(m//(k+1)))

end=time.time()
print("time :", end - start) # 수행 시간 출력