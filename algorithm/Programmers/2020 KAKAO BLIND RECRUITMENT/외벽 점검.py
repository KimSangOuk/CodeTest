from itertools import permutations # 조합

# 원을 돌리는 함수
def spin(weak,n,k):
    new_list=list()
    for i in weak:
        if i+k>n-1:
            i=i+k-n
        else:
            i+=k
        new_list.append(i)
    new_list.sort()
    return new_list

def solution(n, weak, dist):
    # 원에 막대 놓기
    # 취약지점 갯수만큼
    least=len(dist)
    count=0
    # 막대가 올 수 있는 순서의 모든 가짓수
    case_dist=list(permutations(dist,len(dist)))
    for i in range(len(weak)):
        num=0
        # 원 시작점에 취약지점이 오도록
        tmp_list=spin(weak,n,n-weak[i])

        # 라인 생성
        line=[0]*(tmp_list[len(tmp_list)-1]+1)
        # 라인의 취약지점 표시
        for t in range(len(line)):
            if t in tmp_list:
                line[t]=1
        
        
        for case in case_dist:
            stick_num=0
            t=0
            while t<len(line):
                if line[t]==1:
                    if stick_num<len(case):
                        num+=1
                        if t+(case[stick_num])<len(line):
                            t+=(case[stick_num])
                            stick_num+=1
                            
                        elif t+(case[stick_num])>=len(line):
                            break
                    elif stick_num==len(case):
                        count+=1
                        break
                    else:
                        break
                t+=1
            least=min(least,num)
            num=0
    if count==len(case_dist)*len(weak):
        least=-1
        
    return least