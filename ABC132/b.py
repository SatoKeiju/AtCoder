def main():
    n = int(input())
    p = list(map(int, input().split()))

    cnt = 0
    for i in range(n-2):
        if p[i+1] == sorted(p[i:i+3])[1]:
            cnt += 1

    print(cnt)


if __name__ == '__main__':
    main()
