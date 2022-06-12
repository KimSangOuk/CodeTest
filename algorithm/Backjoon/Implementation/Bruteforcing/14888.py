from itertools import permutations

n=int(input())

data=list(map(int,input().split()))
data2=list(map(int,input().split()))

sign_list=list()
for i in range(4):
  if i==0:
    sign='+'
  elif i==1:
    sign='-'
  elif i==2:
    sign='*'
  elif i==3:
    sign='//'
  for j in range(data2[i]):
    sign_list.append(sign)

cases=set(list(permutations(sign_list,len(sign_list))))
form=''

max_result=-1000000001
min_result=1000000001
for case in cases:
  mid=str(data[0])
  for c in range(len(case)):
    if case[c]=='//' and int(mid)<0:
      form+=str(-mid)+case[c]
      form+=str(data[c+1])
      mid=-eval(form)
    else:
      form+=str(mid)+case[c]
      form+=str(data[c+1])
      mid=eval(form)
      
    form=''
    
  min_result=min(mid,min_result)
  max_result=max(mid,max_result)
  form=''
  

print(max_result)
print(min_result)
