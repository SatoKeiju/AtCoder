def main() -> None:
    n, k = map(int, input().split())
    candles = tuple(map(int, input().split()))

    answer = float('inf')
    for i in range(n-k+1):
        l, r = candles[i], candles[i+k-1]
        l2r = abs(l) + abs(r-l)
        r2l = abs(r) + abs(l-r)
        answer = min([answer, l2r, r2l])
    print(answer)


if __name__ == '__main__':
    main()
