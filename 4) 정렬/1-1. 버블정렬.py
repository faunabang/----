li=[9,8,3,4,7]
탐색,바꿈=0,0
print(li)
print("-----------------------------")


for i in range(len(li)-1,0,-1):
    for j in range(i):
        if li[j]>li[j+1]: li[j],li[j+1]=li[j+1],li[j]; 바꿈+=1
        탐색+=1
    print(li,탐색,바꿈)


print("-----------------------------")
print(li)
print(f"탐색: {탐색}\n바꿈: {바꿈}")