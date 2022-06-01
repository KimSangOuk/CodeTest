def solution(n, build_frame):
    # 기둥과 보의 상태
    answer = [[]]
    # 기둥과 보를 쌓을 전체 도면
    data=[[0]*n for _ in range(n)]
    
    build_list=list()
    
    for order in build_frame:
        # 명령의 x,y 좌표
        x=order[0]
        y=order[1]
        # 명령의 x,y 이어지는 좌표
        next_x=0
        next_y=0
        # 명령의 타입 : 0-기둥, 1-보
        build_type=order[2]
        # 명령의 설치 or 제거 : 0-제거, 1-삭제
        install=order[3]
        # 타입별 이어지는 좌표
        if build_type==0:
            next_x=x
            next_y=y+1
        else:
            next_x=x+1
            next_y=y
        order_build=[x,y,next_x,next_y]
        # 설치나 제거
        if install==1:
            build_list.append(order_build)
        else:
            if order_build in build_list:
                build_list.remove(order_build)
                
        isok=test_data(build_list)
        if isok==False:
            if install==1:
                build_list.remove(order_build)
            else:
                build_list.append(order_build)
    
    for k in build_list:
        if k[0]!=k[2] and k[1]==k[3]:
            answer.append([k[0],k[1],1])
        else:
            answer.append(k[0],k[1],0)
    
    # x좌표, y좌표, 종류 순으로 오름차순 정렬
    answer.sort(key=lambda x:[x[0], x[1], x[2]])
    return answer

def test_data(build_list):
    