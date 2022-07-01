import copy

# 균형잡힌 괄호 문자열
def balanced_string(w):
    count1,count2=0,0
    u=''
    v=''
    for i in w:
        if i=='(':
            count1+=1
        elif i==')':
            count2+=1
        u+=i
        if count1==count2:
            v=w[count1*2:len(w)]
            break
    return u,v

# 올바른 괄호 문자열
def correct_string(w):
    stack=list()
    result=True
    for i in w:
        if i=='(':
            stack.append(i)
        elif i==')' and len(stack)==0:
            result=False
            break
        elif i==')':
            stack.pop()
    if len(stack)!=0:
        result=False
    return result

def solution(p):
    # 1. 입력이 빈 문자열일 경우, 빈 문자열 반환
    if len(p)==0:
        return ''

    # 2. 문자열 w -> 균형잡인 괄호 문자열 u와 v로 분리
    # u - 균형잡힌 괄호 문자열로 더 이상 분리 되면 안됨, v - 빈 문자열 가능
    w=copy.deepcopy(p)
    u,v=balanced_string(w)

    # 3. 수행한 결과 문자열을 u에 붙여서 반환
    # 3-1. u가 올바른 괄호 문자열이라면 문자열 v에 대해 1부터 수행
    if correct_string(u):
        u+=solution(v)
    # 4. u가 올바른 괄호 문자열이 아니라면
    else:
        # 4-1. 빈 문자열에 첫문자로 '('을 붙임
        new_string='('
        # 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙임
        new_string+=solution(v)
        # 4-3. ')'를 다시 붙임
        new_string+=')'
        # 4-4. u의 첫번째와 마지막 문자를 제거하고 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙임
        u=u[1:len(u)-1]
        for i in u:
            if i=='(':
                new_string+=')'
            else:
                new_string+='('
        # 4-5. 생성된 문자열 반환
        return new_string
        
    answer = u
    return answer