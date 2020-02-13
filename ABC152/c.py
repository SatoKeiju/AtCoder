def main():
    n = int(input())
    ps = list(map(int, input().split()))

    cnt = 0
    tmp_min = ps[0]
    for p in ps:
        if p <= tmp_min:
            cnt += 1
            tmp_min = p

    print(cnt)


if __name__ == '__main__':
    main()
