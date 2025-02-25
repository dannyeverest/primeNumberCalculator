def clean(x):
    x.remove(1)                                 #removes 1 from list since it's not a prime number
    for i in x:
        if i != 2 and i % 2 == 0:               # excludes 2 since it's even and a prime number and also creates conditions to remove even numbers since they are not prime numbers. 
            x.remove(i)


x = list(range(100000))                              # sets list range of prime numbers for prime numbee analysis 
clean(x)
primeCheck = []                                 #Initialized empty list for adding number of remainderless divisions of potential prime number
primes = []                                     #Initialized empty list to store prime numbers
for i in x:                                     
    for j in range(3,i):                       
        if i % j == 0:
            primeCheck.append(i)
            break
    if len(primeCheck) < 1:
    primeCheck.clear()                          
print(len(primes))
