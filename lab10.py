# get_divisors.py

# 정수를 입력받아 그 수의 약수를 출력하는 프로그램
n = int(input("Enter a number: "))

print("Divisors of", n, "are:")
for i in range(1, n + 1):
    if n % i == 0:
        print(i)
