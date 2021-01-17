def main() -> None:
    n = int(input())
    numbers = [int(input()) for _ in range(n)]

    first = max(numbers)
    second = sorted(numbers)[-2]
    for i, number in enumerate(numbers):
        if number == first:
            print(second)
        else:
            print(first)


if __name__ == '__main__':
    main()
