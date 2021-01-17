def calculate_sum(start: int, end: int) -> int:
    if (end-start) % 2 == 0:
        return ((start+end)*(end-start+1)) // 2
    else:
        return (start+end) * ((end-start+1)//2)


def main() -> None:
    n = int(input())

    answer = 0
    for _ in range(n):
        a, b = map(int, input().split())
        answer += calculate_sum(a, b)
    print(answer)


if __name__ == '__main__':
    main()
