def main() -> None:
    n = int(input())

    for i in range(1, int(n**0.5)+1):
        if n%i == 0 and n//i <= 9:
            print('Yes')
            return
    print('No')


if __name__ == '__main__':
    main()
