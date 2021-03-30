def main() -> None:
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    a = [a_i for a_i in a if a_i != x]
    print(*a)


if __name__ == '__main__':
    main()
