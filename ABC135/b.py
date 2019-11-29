def main():
    n = int(input())
    ps = list(map(int, input().split()))

    cnt = 0
    for i, p in enumerate(ps):
        if i + 1 != p:
            cnt += 1

    print('YES' if cnt <= 2 else 'NO')


if __name__ == '__main__':
    main()
