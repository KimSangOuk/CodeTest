def solution(key, lock):
    answer = True
    rotate_count=0
    
    lock_length=len(lock)
    key_length=len(key)

    expand_lock_length=lock_length+2*key_length
    
    # 옮기기
    expand_lock=[[0]*expand_lock_length for i in range(expand_lock_length)]
    for i in range(key_length,key_length+lock_length):
        for j in range(key_length,key_length+lock_length):
            expand_lock[i][j]=lock[i-key_length,j-key_length]
         
    while rotate_count<4:
        
        
        # 자물쇠 부분 확인
        count=0
        for i in range(key_length,key_length+lock_length):
            for j in range(key_length,key_length+lock_length):
                if expand_lock[i][j]==1:
                    count+=1
        if count==lock_length*lock_length:
            answer=True
            break
        else:
            answer=False
            
        key = array_rotate(key)
        rotate_count+=1
    
    return answer

def array_rotate(array,direction):
    height=len(array)
    width=len(array[0])

    array_complete=[[0]*height for i in range(width)]

    if direction==True:
        for i in range(height):
            for j in range(width):
                array_complete[j][width-1-i]=array[i][j]
    else:
        for i in range(height):
            for j in range(width):
                array_complete[height-j-1][i]=array[i][j]

    return array_complete
