def main() -> None:
    n = int(input())

    points = []
    for _ in range(n):
        points.append(tuple(map(int, input().split())))
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                x3, y3 = points[k]
                if (y2-y1)*(x3-x1) == (y3-y1)*(x2-x1):
                    print('Yes')
                    return
    print('No')


if __name__ == '__main__':
    main()
