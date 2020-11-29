import math


def isPrime(n):
    if (n == 2) or (n == 3):
        return True
    if (n % 6 == 1) or (n % 6 == 5):
        for i in range(2, int(math.sqrt(n) + 1)):
            if n % i == 0:
                return False
        return True
    return False


print(isPrime(11))