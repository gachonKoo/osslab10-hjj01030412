import sys

def get_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

if __name__ == "__main__":
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    else:
        n = int(input())
    print(get_divisors(n))
