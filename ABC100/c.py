def count_division2(x: int) -> int:
    count = 0
    while True:
        if x%2 == 0:
            count += 1
            x = x // 2
        else:
            return count


def main() -> None:
    n = int(input())
    numbers = tuple(map(int, input().split()))

    answer = 0
    for number in numbers:
        answer += count_division2(number)
    print(answer)


if __name__ == '__main__':
    main()
