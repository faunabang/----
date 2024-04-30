rear, front = 1, 1

def q_push(s):
    global rear
    q[rear] = s  # 큐에 요소를 추가
    print(q)
    rear += 1    # rear 포인터를 증가

def bfs(s):
    global front, rear
    q_push(s)  # 시작 정점을 큐에 삽입
    visited[s] = 1  # 시작 정점을 방문 처리
    print(f"{s} 방문")  # 방문한 정점 출력
    while front < rear:  # 큐가 빌 때까지 반복
        u = q[front]  # 큐에서 정점을 꺼냄
        front += 1  # front 포인터를 증가
        for v in range(1, len(g[u])):  # 인접 정점 탐색
            if g[u][v] == 1 and visited[v] == 0:  # v가 u에 인접하고 아직 방문하지 않았다면
                q_push(v)  # 큐에 v를 삽입
                visited[v] = 1  # v를 방문 처리
                print(f"{v} 방문")  # 방문한 정점 출력

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
visited = [0 for _ in range(6)]
# 큐 초기화
q = [0 for _ in range(100)]
# 너비우선탐색 시작
bfs(1)
