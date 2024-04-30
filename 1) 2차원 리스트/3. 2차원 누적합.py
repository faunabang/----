# n을 입력받는다.
# n*n개의 값을 무작위로 입력받는다.
# 각 행과 열 요소의 값들을 누적한 n*n 행렬을 출력한다.

n=3
li=[[0]*(n+1) for _ in range(n+1)]
cols=[[i+1 for i in range(j,j+n*n,n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        li[i+1][j+1]=cols[i][j]
print(*li, sep="\n"); print("")

sum=[[0]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        sum[i][j]=li[i][j]+sum[i-1][j]+sum[i][j-1]-sum[i-1][j-1]

print(*sum, sep="\n")