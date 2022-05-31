def solution(key, lock):
    rotate_count=0
    
    lock_length=len(lock)
    key_length=len(key)

    expand_lock_length=lock_length+2*key_length

    while rotate_count<4:
        for i in range(key_length+lock_length+1):
            for j in range(key_length+lock_length+1):

                expand_lock=[[0]*expand_lock_length for i in range(expand_lock_length)]
                for w in range(key_length,key_length+lock_length):
                    for t in range(key_length,key_length+lock_length):
                        expand_lock[w][t]=lock[w-key_length][t-key_length]
              
                for k in range(key_length):
                    for l in range(key_length):
                        if (key[k][l]==1 and expand_lock[k+i][l+j]==0) or key[k][l]==0 and expand_lock[k+i][l+j]==1:
                            expand_lock[k+i][l+j]=1
                        else:
                            expand_lock[k+i][l+j]=0

                count=0
                for w in range(key_length,key_length+lock_length):
                    for t in range(key_length,key_length+lock_length):
                        if expand_lock[w][t]==1:
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