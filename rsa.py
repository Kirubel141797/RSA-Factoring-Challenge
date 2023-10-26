#!/usr/bin/python3
import sys
import math
import random

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def pollards_rho(n):
    if n % 2 == 0:
        return 2
    x = random.randint(1, n-1)
    y = x
    c = random.randint(1, n-1)
    d = 1  
    while d == 1:
        x = (x*x + c) % n
        y = (y*y + c) % n
        y = (y*y + c) % n
        d = gcd(abs(x-y), n)
        if d == n:
            return pollards_rho(n)
    return d

def factorize(n):
    if n <= 1:
        return []
    prime = pollards_rho(n)
    if prime == n:
        return [n]
    return factorize(prime) + factorize(n // prime)

def main():
    if len(sys.argv) != 2:
        print("Usage: rsa <file>")
        return

    file_path = sys.argv[1]
    with open(file_path, 'r') as file:
        n = int(file.read().strip())
        factors = factorize(n)
        print(f"{n}={factors[0]}*{factors[1]}")

if __name__ == "__main__":
    main()
