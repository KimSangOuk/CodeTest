def solution(s):
    length=len(s)
    
    new_list=list()
    new_s=''
    least=1000
    
    if length==1:
        least=1
    else:
        for i in range(1,length//2+1):
            t=0
            count=1
            while length-1>=t:
                new_list.append(s[t:t+i])
                t+=i
            for j in range(len(new_list)):
                if j!=len(new_list)-1 and new_list[j]==new_list[j+1]:
                    count+=1
                else:
                    if count!=1:
                        new_s+=str(count)+new_list[j]
                    else:
                        new_s+=new_list[j]
                    count=1
            if len(new_s)<least:
                least=len(new_s)
            new_s=''
            new_list.clear()
    return least