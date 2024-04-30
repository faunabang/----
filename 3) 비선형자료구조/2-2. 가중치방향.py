import random

n=int(input("vertex: "))
e=int(input("edge: "))
g=[[0]*(n+1) for _ in range(n+1)]
print(*g,sep="\n")
for i in range(e):
    v1,v2,w=map(int,input().split(" "))
    g[v1][v2]=w
    print(*g,sep="\n")