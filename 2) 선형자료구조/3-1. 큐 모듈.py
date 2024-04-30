import queue
q=queue.Queue() # 큐 생성
q.put(1)  # 큐에 자료 입력하기
q.put(2)
q.get()   # 큐에서 자료하나 빼내기. 1삭제
q.put(3)
q.get()   # 큐에서 자료하나 빼내기. 2삭제
q.get()   # 큐에서 자료하나 빼내기. 3삭제
