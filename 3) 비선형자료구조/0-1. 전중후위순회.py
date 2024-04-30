'''
다음과 같이 어떤 트리가 완전이진트리의 형태로 입력이 된다고 할때, 중위순회한 결과를 출력하는 프로그램을 작성하시오.
입력) ABCDEFGHI              
출력) HDIBEAFCG
'''

def inorder(k):
  if k<=len(tree)-1: #___종결조건____
    inorder(2*k+1)#  _왼쪽서브트리 중위순회_
    print(tree[k],end="")#  ___루트출력___
    inorder(2*k+2)#  _오른쪽서브트리 중위순회_
  else:
    return

# tree=list(input())
tree=list("ABCDEFGHI")
inorder(0)