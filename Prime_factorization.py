from math import sqrt
userInput=int(input()) 
primefac=""
while userInput%2==0:
    primefac=primefac+" "+str(2)
    userInput=userInput/2 
for var in range(3,int(sqrt(userInput))+1,2):
    while userInput%var==0:
        primefac=primefac+" "+str(var)
        userInput=userInput/var
 print(primefac)
