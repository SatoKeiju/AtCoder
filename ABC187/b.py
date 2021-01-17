def main() -> None:
    n = int(input())
    points = [tuple(map(int, input().split())) for _ in range(n)]

    answer = 0
    for i in range(n-1):
        for j in range(i+1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]
            if -1 <= (y2-y1)/(x2-x1) <= 1:
                answer += 1
    print(answer)


if __name__ == '__main__':
    main()
