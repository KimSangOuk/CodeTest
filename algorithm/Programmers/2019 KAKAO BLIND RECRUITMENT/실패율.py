def solution(N, stages):
    answer = [] # 실패율을 내림차순으로 정렬한 번호
    stages.sort()
    unclear_player=[0]*N # 각 단계별 클리어 못한 사람 수
    unclear_percent=[0]*N # 각 단계별 실패율
    sum_player=len(stages) # 총 플레이어 수
    # 각 단계별 클리어 못한 사람 수 분별
    for i in stages:
        if not i==N+1:
            unclear_player[i-1]+=1
    # 실패율 구하기
    for i in range(N):
        # 깬 사람이 0명이 아닐때
        if unclear_player[i]!=0:
            unclear_percent[i]=(i,unclear_player[i]/sum_player)
        # 0명일때
        else:
            unclear_percent[i]=(i,0)
        # 앞 단계에서 실패한 사람 감소
        sum_player-=unclear_player[i]
    # 실패율을 기준으로 정렬
    unclear_percent.sort(key=lambda x:(x[1]),reverse=True)
    # 각 스테이지 기준으로 답 도출
    for i in range(N):
        answer.append(unclear_percent[i][0]+1)
    return answer

n=5	
stages=[2, 1, 2, 6, 2, 4, 3, 3]
print(solution(n,stages))

n=4	
stages=[4,4,4,4,4]
print(solution(n,stages))