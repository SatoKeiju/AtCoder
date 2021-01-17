def main() -> None:
    a, b, x = map(int, input().split())

    l, r = 0, 1000000001
    while (r-l) > 1:
        n = (l+r) // 2
        cost = a*n + b*len(str(n))
        if cost <= x:
            l = n
        else:
            r = n
    print(l)


if __name__ == '__main__':
    main()
