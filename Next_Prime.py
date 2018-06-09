from gmpy2 import next_prime
counter=1
nextPrime=""
while True:
    userInput=int(input())#1 to next 0 to exit
    if userInput == 1:
        counter=counter+1
        nextPrime=nextPrime+" "+str(next_prime(counter))
    else:
        break
print(nextPrime)
