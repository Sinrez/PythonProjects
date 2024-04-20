import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

primes = [i for i in range(1, 20) if is_prime(i)]
print(primes)