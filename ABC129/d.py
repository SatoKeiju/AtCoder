def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]

    l = [[0] * w for _ in range(h)]
    r = [[0] * w for _ in range(h)]
    u = [[0] * w for _ in range(h)]
    d = [[0] * w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if s[i][j] == '.':
                l[i][j] = l[i][j-1] + 1
                u[i][j] = u[i-1][j] + 1
            if s[i][-j-1] == '.':
                r[i][-j-1] = r[i][-j] + 1
            if s[-i-1][j] == '.':
                d[-i-1][j] = d[-i][j] + 1

    torch = 0
    for i in range(h):
        for j in range(w):
            torch = max(torch, l[i][j]+r[i][j]+u[i][j]+d[i][j]-3)

    print(torch)


if __name__ == '__main__':
    main()
