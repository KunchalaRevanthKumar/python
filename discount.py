#applying discount in shopping malls
n=int(input())
c=input()
if((n>=1000 and n<=2000) and (c=='R' or c=='r' or c=='N' or c=='n')):
    if c=='r' or c=='R':
        print(n)
        b=0
        print("discount =",b)
        print("total=",(n-b))
    else:
        print(n)
        b=0.05*n
        print("discount=",b)
        print("total=",(n-b))
elif((n>=2001 and n<=2999) and (c=='R' or c=='r' or c=='N' or c=='n')):
    if c=='r' or c=='R':
        print(n)
        b=0.05*n
        print("discount =",b)
        print("total=",(n-b))
    else:
        print(n)
        b=0.1*n
        print("discount=",b)
        print("total=",(n-b))
elif(n>=3000 and (c=='R' or c=='r' or c=='N' or c=='n')):
    if c=='r' or c=='R':
        print(n)
        b=0.15*n
        print("discount =",b)
        print("total=",(n-b))
    else:
        print(n)
        b=1.5*n
        print("discount=",b)
        print("total=",(n-b))
else:
    print("no discount")





    



        
        
    
        
