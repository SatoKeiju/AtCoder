def main() -> None:
    l = int(input())

    numerator, denominator = 1, 1
    for i in range(1, 12):
        numerator *= l - i
        denominator *= i
    print(numerator // denominator)


if __name__ == '__main__':
    main()
