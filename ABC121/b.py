def main():
    n, m, c = map(int, input().split())
    b = input().split()
    cnt = 0

    for i in range(n):
        a = input().split()
        sum = 0
        for ai, bi in zip(a, b):
            sum += int(ai)*int(bi)
        if sum + c > 0:
            cnt += 1

    print(cnt)


if __name__ == '__main__':
    main()
