def primeSieve(n):
    primes = [[x,True] for x in range(0,n+1)]
    for i in range(2,n//2+1):
        temp = 2*i
        while temp <= n:
            primes[temp][1] = False
            temp += i
    sieve = [x[0] for x in primes if x[1]]
    return sieve[2:]

x = primeSieve(10**8)

print (len(x))
