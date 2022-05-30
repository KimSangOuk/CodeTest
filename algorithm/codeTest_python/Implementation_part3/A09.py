s=input()
length=len(s)

answer = 0
length=len(s)
    
new_list=list()
new_s=''
least=1000
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
    print(new_s)
    new_s=''
    new_list.clear()
    # if answer<least:
    #   least=answer

# print(least)