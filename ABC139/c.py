def main():
    n = int(input())
    hs = list(map(int, input().split()))

    cnt = 0
    cnt_max = 0
    for i in range(n-1):
        if hs[i] >= hs[i+1]:
            cnt += 1
            cnt_max = max(cnt, cnt_max)
        else:
            cnt_max = max(cnt, cnt_max)
            cnt = 0

    print(cnt_max)


if __name__ == '__main__':
    main()
