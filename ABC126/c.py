def main():
    n, k = map(int, input().split())

    win_prob = 0

    import math
    if n < k:
        for i in range(1, n+1):
            win_prob += 0.5 ** math.ceil(math.log2(k / i))
        print(win_prob / n)
    else:
        for i in range(1, k):
            win_prob += 0.5 ** math.ceil(math.log2(k / i))
        print(win_prob / n + (n - k + 1) / n)


if __name__ == '__main__':
    main()
