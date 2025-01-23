import time
import random


def find_factors(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
            time.sleep(0.00001)
    return factors


def main():
    upper_limit = 10000
    for num in range(1, upper_limit + 1):
        factors = find_factors(num)
        print(f"{num} 的因数有：{factors}")
        print(random.randint(1, 10000))


while True:
    main()
