
### iterative
def fibonacci_iter(n):
    if n < 0:
        raise ValueError("n must be > 0")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 0
        b = 1
        for i in range (n-1):
            c = a + b
            a = b
            b = c
        return b


################ recursive

def fibonacci_rec(n):
    if n < 0:
        raise ValueError('n must be > 0')
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_rec(n-1) + fibonacci_rec(n-2)

if __name__ == '__main__':


    print([fibonacci_iter(num) for num in range(12)])

    ### cal rec case
    print([fibonacci_rec(num) for num in range(12)])