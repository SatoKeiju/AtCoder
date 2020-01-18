def main():
    n, k, m = map(int, input().split())
    results = list(map(int, input().split()))

    border = n * m - sum(results)

    print(max(0, border) if border <= k else -1)


if __name__ == '__main__':
    main()
