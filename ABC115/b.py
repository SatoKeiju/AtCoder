def main():
    n = int(input())
    prices = [int(input()) for _ in range(n)]

    print(sum(prices) - max(prices) // 2)


if __name__ == '__main__':
    main()
