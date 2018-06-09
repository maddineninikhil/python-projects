userInput=int(input())
if userInput == 1:
    print('0')
elif userInput == 2:
    print('0 1')
else:
    fib="0 1"
    prev1=0
    prev2=1
    for var in range(2,userInput,1):
        result=prev1+prev2
        fib=fib+" "+str(result)
        prev1=prev2
        prev1=result
    print(fib)
        
        
