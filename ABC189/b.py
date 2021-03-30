def main() -> None:
    n, x = map(int, input().split())

    x *= 100
    total = 0
    for i in range(1, n+1):
        v, p = map(int, input().split())
        alcohol = v * p
        total += alcohol
        if total > x:
            print(i)
            return
    print(-1)


if __name__ == '__main__':
    main()
