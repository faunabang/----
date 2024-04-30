# n입력하면 n행의 파스칼의 삼각형을 출력하는 프로그램을 만들어보자.
n=10
li=[[0 for i in range(j)] for j in range(1,n+1)]
for i in range(n):
    for j in range(len(li[i])):
        if j== 0 or j==i:
            li[i][j]=1
        else:
            li[i][j]=li[i-1][j]+li[i-1][j-1]

print(*li, sep="\n")