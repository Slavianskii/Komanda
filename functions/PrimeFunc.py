import math


class TestClass:

    def __init__(self):
        pass

    def isPrime(self, num):
        if num <= 0: return -1
        for i in range(2, int(math.sqrt(num) + 1)):
            if num % i == 0: return 0
        return 1
