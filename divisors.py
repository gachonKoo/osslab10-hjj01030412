import sys

def get_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

if __name__ == "__main__":
    # 우선 명령행 인자 확인
    if len(sys.argv) > 1:
        try:
            n = int(sys.argv[1])
        except:
            # 만약 인자가 정수가 아니면 표준입력으로 시도
            data = sys.stdin.read().strip()
            n = int(data) if data else 0
    else:
        # 인자가 없으면 표준입력에서 읽음 (예: echo 100 | python divisors.py)
        data = sys.stdin.read().strip()
        n = int(data) if data else 0

    print(get_divisors(n))
