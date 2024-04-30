import queue

def bfs(s):
    q.put(s)
    visited[s]=1

    while q:
        s=q.get() # s 변경!!!
        print(s)

        for i in range(1,len(g)):
            if g[s][i]==1 and visited[i]==0:
                q.put(i)
                visited[i]=1

# 그래프를 인접 행렬로 표현
g = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 0]
]

# 방문 상태 배열
visited = [0 for _ in range(len(g))]
q=queue.Queue()
bfs(1)
