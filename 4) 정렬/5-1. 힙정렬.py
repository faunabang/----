import heapq
li=[1,6,2,8,9,3,0,5,4,7]
heapq.heapify(li)
sorted=[heapq.heappop(li) for i in range(len(li))]
print(sorted)

# import heapq
# v=[23,12,16,13,32,8,2,24,47,26]
# heapq.heapify(v)
# print(v)
# sorted = []
# while v:
#   sorted.append(heapq.heappop(v))
# print(sorted)