def main() -> None:
    n, x = map(int, input().split())
    s = input()

    for result in s:
        if result == 'o':
            x += 1
        else:
            x = max(x-1, 0)

    print(x)


if __name__ == '__main__':
    main()
