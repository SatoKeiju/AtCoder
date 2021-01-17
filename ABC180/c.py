def main() -> None:
    n = int(input())

    border = int(n ** 0.5)
    memo = []
    for i in range(1, border+1):
        if n % i == 0:
            print(i)
            memo.append(n // i)

    if border ** 2 == n:
        memo.pop(-1)
    for number in memo[::-1]:
        print(number)


if __name__ == '__main__':
    main()
