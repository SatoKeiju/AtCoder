def main() -> None:
    n = int(input())

    for i in reversed(range(1, int(n**0.5)+1)):
        if n % i == 0:
            print(i + n//i - 2)
            return


if __name__ == '__main__':
    main()
