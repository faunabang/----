# 174쪽 DFS -교과서 예제 프로그램, 인접행렬

def dfs(n):
  visited[n]=1
  print(n)
  for i in range(1,len(g)):
    if g[n][i]==1 and visited[i]==0: # n번 정점과 연결이 되어있고 아직 방문하지 않았다면
      dfs(i)


g=[[0,0,0,0,0,0,0,0,0],
   [0,0,1,1,0,0,0,0,0],
   [0,1,0,0,1,1,0,0,0],
   [0,1,0,0,0,0,1,1,0],
   [0,0,1,0,0,0,0,0,1],
   [0,0,1,0,0,0,0,0,1],
   [0,0,0,1,0,0,0,0,1],
   [0,0,0,1,0,0,0,0,1],
   [0,0,0,0,1,1,1,1,0]]

visited=[0 for _ in range(len(g))]
dfs(1)


# v,e,rt=map(int, input().split())
# graph=[[0]*(v+1) for i in range(v+1)]
# for i in range(e):
#   a,b=map(int,input().split())
#   graph[a][b],graph[b][a]=1,1

# for i in range(1,v+1):
#   for j in range(1,v+1):
#     print(graph[i][j],end='')
#   print()