def clean(x):                                   #defines function to remove even number above 2 and the number 1  
    x.remove(1)                                 #removes 1 from list since it's not a prime number
    for i in x:
        if i != 2 and i % 2 == 0:               # excludes 2 since it's even and a prime number and also creates conditions to remove even numbers since they are not prime numbers. 
            x.remove(i)


x = list(range(100001))                              # sets list range of prime numbers for prime numbee analysis 
clean(x)
primeCheck = []                                 #Initialized empty list for adding number of remainderless divisions of potential prime number
primes = []                                     #Initialized empty list to store prime numbers
for i in x:                                     #Loops over cleaned range of x
    for j in range(1,i+1):                      #nested loop of the current interated number in x and every number less than it and checks if it factors without a remainder. 
        if i % j == 0:                          #if it factor with no remainder
            primeCheck.append(i)                #if there's no remainder add it to the primeCheck list
    if len(primeCheck) == 2:                    #if the primeChech list length is 2...
        primes.append(i)                        #add the number to my list of primes
    primeCheck.clear()                          #clear primeCheck for the next primeCheck
print(len(primes))