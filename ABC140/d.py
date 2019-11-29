def main():
    n, k = map(int, input().split())
    s = input()

    which = s[0]
    init_sum = 0
    for i in range(1, n):
        if s[i] == which:
            init_sum += 1
        else:
            which = s[i]

    print(min(init_sum + 2*k, n-1))


if __name__ == '__main__':
    main()
