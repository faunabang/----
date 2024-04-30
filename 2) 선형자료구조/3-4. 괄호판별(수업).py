a=list(input())
stk=[]
flag=0
for x in a:
    if x=='(': stk.append(x) #여는 괄호 ‘(‘ 이면 스택에 추가
    elif x==')':
      if len(stk)==0: flag=1; break
      else: stk.pop() #닫는 괄호 ‘)’ 이면 스택에서 pop

if len(stk)==0 and flag==0:
    print('good')
else:
    print('bad')