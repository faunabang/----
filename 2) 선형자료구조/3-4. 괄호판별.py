'''
괄호 문자열이 주어지면 올바른 괄호 문자열인지 판단하는 프로그램을 작성하시오.
올바른 괄호 문자열이란 여는 괄호와 닫는 괄호의 짝이 맞고, 포함 관계에 문제가 없는 문자열을 말한다.
예를 들어, 
) ( ) (  인 경우 여는 괄호와 닫는 괄호의 짝이 맞지 않으므로 올바른 괄호 문자열이 아니다.
( ( ) ( ) ) 인 경우 괄호의 짝이 맞고 포함 관계가 맞으므로 올바른 괄호 문자열이다.
'''

c1="(()())"
c2="(())()((())())(()())"
w1="()((()))())())())"
w2=")()("

def determine(b):
    b=list(b)
    stk=[]
    flag=-1
    for i in range(len(b)):
        if b[i]=="(":
            stk.append(1)
        elif b[i]==")":
            if len(stk)==0: flag=i; break
            else: stk.pop()
    if len(stk)==0 and flag==-1:
        print("correct")
    else: print(f"incorrect in >> {flag} <<")


determine(c1)
determine(c2)
determine(w1)
determine(w2)