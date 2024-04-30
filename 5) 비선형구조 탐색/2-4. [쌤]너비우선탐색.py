# 쌤코드
'''인접행렬 >> 관계 없는 것도 나타냄 >> 메모리 낭비'''

rear,front=1,1

def q_push(s):
  global rear
  q[rear]=s
  rear+=1

def bfs(s):
  global rear,front
  q_push(s)
  visited[s]=1
  while rear>front:
    s=q[front]
    print(s)
    front+=1
    for i in range(1,6):
      if g[s][i]==1 and visited[i]!=1:
        q_push(i)
        visited[i]=1
      print(q)

g=[[0,0,0,0,0,0],
   [0,0,1,0,1,0],
   [0,1,0,0,0,0],
   [0,0,0,0,1,0],
   [0,1,0,1,0,1],
   [0,0,0,0,1,0]]
visited=[0 for _ in range(6)]
q=[0 for _ in range(100)]
bfs(1)