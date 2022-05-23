n=input()

front=0
back=0

for i in range(len(n)):
  if i<len(n)/2:
    front+=int(n[i])
  else:
    back+=int(n[i])

if front==back:
  print("LUCKY")
else:
  print("READY")