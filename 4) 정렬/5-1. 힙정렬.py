import heapq
li=[1,6,2,8,9,3,0,5,4,7]
heapq.heapify(li)
sorted=[heapq.heappop(li) for i in range(len(li))]
print(sorted)