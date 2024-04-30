'''
# 그래프의 저장
2차원 리스트를 이용하여 무방향 그래프를 인접행렬로 저장하는 프로그램을 작성하시오.
(입력 첫째줄) 정점의갯수, 간선의 갯수
(입력 둘째줄~) 두 정점의] 간선 정보(간선의 갯수만큼)
'''

# n=5
# g=[[0]*(n+1) for _ in range(n+1)]
# print(*g,sep="\n")

n=int(input("vertex: "))
e=int(input("edge: "))
g=[[0]*(n+1) for _ in range(n+1)]
print(*g,sep="\n")
for i in range(e):
    a,b=map(int,input().split(" "))
    g[a][b],g[b][a]=1,1
    print(*g,sep="\n")