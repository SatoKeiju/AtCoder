def main():
    n, x = map(int, input().split())
    distances = list(map(int, input().split()))

    d = 0
    cnt = 1
    for l in distances:
        d += l
        if d <= x:
            cnt += 1
        else:
            break

    print(cnt)


if __name__ == '__main__':
    main()
