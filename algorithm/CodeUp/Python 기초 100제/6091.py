from math import lcm

a,b,c=map(int,input().split())
print(lcm(lcm(a,b),c))