# n*n개의 정수 입력, n개씩 줄을 바꾸어 출력하기
# 한줄에 공백구분으로 입력받기

n=5
rows=[[i+1 for i in range(n*j,n*(j+1))] for j in range(n)]
print(*rows, sep="\n")