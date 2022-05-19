# https://programmers.co.kr/learn/courses/30/lessons/42891

# solution.py

from collections import deque
def solution(food_times, k):
    q=deque()
    
    for i in range(len(food_times)):
        q.append(i)
    
    for i in range(k):
        d=q.popleft()
        if food_times[d]>1:
            q.append(d)
        food_times[d]-=1
        
    if len(q)==0:
        answer = -1
    else:
        answer = q.popleft()+1
    return answer