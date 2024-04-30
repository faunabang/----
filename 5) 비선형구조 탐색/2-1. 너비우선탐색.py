rear,front=1,1

def q_push(s):
  global rear
  q[rear]=s
  rear+=1

def bfs(s):
  global rear # 전역변수 지정
  q_push(s) # s정점 큐에 저장
  visited[s]=1 # s정점 방문처리
  while len(q)>0: # 큐가 빌때까자 다음을 반복
    print(q.pop()) # 큐삭제, 출력, front+1
    # 정점의 갯수만큼 반복
    # n번 정점과 연결이 되어있고 아직 방문하지 않았다면
      # 큐삽입, 방문처리

g=[[0,0,0,0,0,0],[0,0,1,0,1,0],[0,1,0,0,0,0],[0,0,0,0,1,0],[0,1,0,1,0,1],[0,0,0,0,1,0]]
visited=[0 for _ in range(6)]
q=[0 for _ in range(100)]
bfs(1)