li=[9,8,3,4,7]
mindex=0
print(li)
print("------------------------")

for i in range(len(li)-1):
    mindex=i
    for j in range(i,len(li)):
        if li[mindex]>li[j]: mindex=j
    li[mindex],li[i]=li[i],li[mindex]
    print(li)

print("------------------------")
print(li)