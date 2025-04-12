def swipe(n):
    """Print the digits of n, one per line, first backward then forward.

    >>> swipe(2837)
    7
    3
    8
    2
    8
    3
    7
    """
    if n < 10:
        print(n)
    else:
        first, last = n // 10, n % 10
        print (last)
        swipe (first)
        print(last)

def skip_factorial(n):
    """Return the product of positive integers n * (n - 2) * (n - 4) * ...

    >>> skip_factorial(5) # 5 * 3 * 1
    15
    >>> skip_factorial(8) # 8 * 6 * 4 * 2
    384
    """
    if n <=2:
        return n
    else:
        return n * skip_factorial(n - 2)

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    assert n>1, "n must be an integer greater than 1"

    def f(i):
        if n==i:
            return True
        elif n % i == 0:
            return False
        else:
            return f(i+1)
        
    return f(2)

def max_dig(n):
    if n<10:
        return n
    else:
        if max_dig(n//10)>n%10:
            return max_dig(n//10)
        else:
            return n%10

def hailstone(n):
    """Print out the hailstone sequence starting at n, 
    and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    print(n)
    if n % 2 == 0:
        return even(n)
    else:
        return odd(n)

def even(n):
    return 1+hailstone(int(n/2))

def odd(n):
    if n==1:
        return 1
    if n>1:
        return 1+hailstone(int(3*n+1))