def main() -> None:
    numbers = sorted(list(map(int, input().split())))
    k = int(input())

    print(numbers[0] + numbers[1] + numbers[2] * 2**k)


if __name__ == '__main__':
    main()
