# 문제
# 세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.

# 그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.

# 괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 식이 주어진다. 식은 ‘0’~‘9’, ‘+’, 그리고 ‘-’만으로 이루어져 있고, 가장 처음과 마지막 문자는 숫자이다. 그리고 연속해서 두 개 이상의 연산자가 나타나지 않고, 5자리보다 많이 연속되는 숫자는 없다. 수는 0으로 시작할 수 있다. 입력으로 주어지는 식의 길이는 50보다 작거나 같다.

# 출력
# 첫째 줄에 정답을 출력한다.

# 난이도 : silver 2
# 소요 시간 : 01:26:18

import sys

#식 입력받기
data=sys.stdin.readline().rstrip()

string_num=''

form=list()
sum_num=list()
circulate=list()

for i in range(len(data)):
  if data[i]!='+' and data[i]!='-':
    string_num+=data[i]
  else:
    form.append(int(string_num))
    string_num=''
    form.append(data[i])
form.append(int(string_num))

for i in form:
  if i=='-':
    circulate.append(sum(sum_num))
    sum_num.clear()
  elif i!='+':
    sum_num.append(i)

circulate.append(sum(sum_num))

result=circulate[0]
for i in range(1,len(circulate)):
  result-=circulate[i]

print(result)