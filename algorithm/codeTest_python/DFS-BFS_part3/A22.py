from collections import deque

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def solution(board):
    n=len(board)
    q=deque()
    q.append(((0,0),(0,1)))
    state=list()
    state.append(((0,0),(0,1)))
    while q:
        v=q.popleft()
        start,end=v
        # 세로,가로 상관없이 4방향 이동 탐색
        for i in range(4):
            vx_start=start[0]+dx[i]
            vy_start=start[1]+dy[i]
            vx_end=end[0]+dx[i]
            vy_end=end[0]+dy[i]
            # 보드의 범위를 벗어나거나
            if vx_start<0 or vy_start<0 or vx_end<0 or vy_end<0 or vx_start>=n or vy_start>=n or vx_end>=n or vy_end>=n:
                continue
            # 벽에 충돌하거나
            if board[vx_start][vy_start]==1 or board[vx_end][vy_end]==1:
                continue
            # 지나온 경우에 포함된다면
            for i,j in state:
                if (i==(vx_start,vy_start) and j==(vx_end,vy_end)) or (j==(vx_start,vy_start) and i==(vx_end,vy_end)):
                    continue
            q.append(((vx_start,vy_start),(vx_end,vy_end)))
            state.append(((vx_start,vy_start),(vx_end,vy_end)))
        # 세로일 경우
        if abs(start[0]-end[0])==1:
          
    # 걸리는 최소 소요 시간
    answer = 0
    return answer

board=[[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
print(solution(board))