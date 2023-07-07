a, b = map(int,input().split())
print("True" if ((not a)or b) and (a or (not b)) else "False")