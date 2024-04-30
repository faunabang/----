import heapq

def heapsort(vv):
  h = []
  for value in vv:
    heapq.heappush(h, value)
  return [heapq.heappop(h) for i in range(len(h))]

v=[23,12,16,13,32,8,2,24,47,26]
print(heapsort(v))