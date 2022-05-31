def solution(key, lock):
    rotate_count=0
    
    lock_length=len(lock)
    key_length=len(key)

    expand_lock_length=lock_length+2*key_length
    
    expand_lock=[[0]*expand_lock_length for i in range(expand_lock_length)]
    for i in range(key_length,key_length+lock_length):
        for j in range(key_length,key_length+lock_length):
            expand_lock[i][j]=lock[i-key_length][j-key_length]

    while rotate_count<4:
        for i in range(key_length+lock_length):
            for j in range(key_length+lock_length):
                for k in range(key_length):
                    for l in range(key_length):
                        if key[k][l]==1:
                            expand_lock[k+i][l+j]=1
                # print(expand_lock)
                # 자물쇠 부분 확인
                count=1
                for i in range(key_length,key_length+lock_length):
                    for j in range(key_length,key_length+lock_length):
                        if expand_lock[i][j]==1:
                            count+=1
        
                if count==lock_length*lock_length:
                    return True
            
        key = array_rotate(key,True)
        rotate_count+=1
    
    return False

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

key=[[0]*3 for i in range(3)]
key[1][0]=1
key[2][1]=1
key[2][2]=1
lock=[[1]*3 for i in range(3)]
lock[1][2]=0
lock[2][1]=0
print(solution(key,lock))