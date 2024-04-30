def p(li):
    print(*li, sep='\n');print("")

# 2차원 리스트 제작
n=5
l1=[[0]*n]*n
l2=[[0 for i in range(n)] for i in range(n)]

p(l1)
p(l2)

l1[1][2],l1[2][3]=1,2
l2[1][2],l2[2][3]=1,2

p(l1)
p(l2)

