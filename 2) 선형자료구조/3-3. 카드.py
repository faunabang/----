def push(q,a):
    q.insert(0,a)

q=[]
N=6
for i in range(1,N+1):
    push(q,i)

while len(q)>1:
    q.pop()
    push(q,q.pop())

print(q.pop())

'''
쌤 버전

# 리스트의 맨 오른쪽이 카드의 맨위.
n=int(input())
q=[i for i in range(n,0,-1)]

while len(q)>1:
  q.pop()
  q.insert(0,q.pop())
print(q)
'''