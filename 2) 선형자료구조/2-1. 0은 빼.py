#0은 빼!
n=int(input())
s=[]
for i in range(n):
  k=int(input())
  if k != 0:
    s.append(k)
  # else: s.pop(len(s)-1)
  else: s.pop()
  print(s)

print("--------------------")
print(sum(s))