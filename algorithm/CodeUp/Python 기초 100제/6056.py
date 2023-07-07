a, b = map(int,input().split())
print("True" if ((not a)and b) or (a and (not b)) else "False")