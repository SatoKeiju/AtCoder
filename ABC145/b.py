def main() -> None:
    n = int(input())
    s = input()

    if n%2 == 0 and s[:n//2] == s[n//2:]:
        print('Yes')
        return
    print('No')


if __name__ == '__main__':
    main()
