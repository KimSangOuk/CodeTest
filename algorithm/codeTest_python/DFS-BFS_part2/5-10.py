# N*M 크기의 얼음 틀
n,m=map(int,input().split())

# N*M 크기의 얼음 틀의 모양
ice_map=list()
for _ in range(n):
  tmp=""
  tmp=input()
  tmp_list=list()
  for i in range(m):
    tmp_list.append(int(tmp[i]))
  ice_map.append(tmp_list)

# 확인용 코드
# for i in range(n):
#   print(ice_map[i])

# 깊이 우선 검색 -> 바로 탐색한 위치 벽으로 처리
def dfs(x, y):
  # 영역 벗어나면 탈출
  if x<0 or y<0 or x>n-1 or y>m-1:
    return
  if ice_map[x][y]==0:
    ice_map[x][y]=1
    # 사방을 탐색
    dfs(x+1,y)
    dfs(x-1,y)
    dfs(x,y+1)
    dfs(x,y-1)
    return True
  return False

# 탐색 시작
count=0
for i in range(n):
  for j in range(m):
    # 탐색이 완료될 경우
    if dfs(i,j)==True:
      count+=1

print(count)