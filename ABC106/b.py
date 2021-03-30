def count_divisor(n: int) -> int:
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    return count


def main() -> None:
    n = int(input())

    answer = 0
    for i in range(1, n+1, 2):
        if count_divisor(i) == 8:
            answer += 1
    print(answer)


if __name__ == '__main__':
    main()
