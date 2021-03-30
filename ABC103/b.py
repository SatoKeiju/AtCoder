def main() -> None:
    s = input()
    t = input()
    for _ in range(len(s)):
        if s == t:
            print('Yes')
            return
        else:
            s = s[1:] + s[0]
    print('No')


if __name__ == '__main__':
    main()
