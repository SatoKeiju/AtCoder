def main():
    n, m = map(int, input().split())

    start, end = 1, n
    for _ in range(m):
        l, r = map(int, input().split())
        if r < start or l > end:
            start, end = 1, 0
            break
        elif l <= start and start <= r <= end:
            end = r
        elif start <= l <= end and end <= r:
            start = l
        elif l <= start and r >= end:
            pass
        else:
            start, end = l, r

    print(end - start + 1)


if __name__ == '__main__':
    main()
