import deque
def solution(food_times, k):
    q=deque()
    
    for i in range(len(food_times)):
        q.append(i)
    
    for i in k:
        d=q.pop()
        if food_time[d]>0:
            food_time[d]-=1
            q.append(d)
        
    answer = q.pop()
    return answer