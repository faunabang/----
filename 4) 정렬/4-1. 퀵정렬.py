def q_sort(a,start,end):
  if start>=end: # 역전
    return
  pivot=start
  left=start+1
  right=end
  while(left<=right):
    while(left<=end and a[left]<=a[pivot]):
      left+=1
    while(right>start and a[right]>=a[pivot]):
      right-=1
    if(left>right):
      a[right],a[pivot]=a[pivot],a[right]
    else:
      a[right],a[left]=a[left],a[right]
    print(a)
  q_sort(a,start,right-1)
  q_sort(a,right+1,end)

def q_sort_rear(a,start,end):
  pivot=end
  left=start
  right=end-1
  while left>right:
    while left<pivot and left<=end: left+=1
    while right>pivot and right>=start: right-=1
    if(left>right):
      a[right],a[pivot]=a[pivot],a[right]
    else:
      a[right],a[left]=a[left],a[right]
    print(a)
  q_sort_rear(a,start,right-1)
  q_sort_rear(a,right+1,end)


li = [8,1,4,9,6,3,5,2,7,0]
q_sort(li,0,len(li)-1)
print("------------------------------------")
q_sort_rear(li,0,len(li)-1)
print(li)