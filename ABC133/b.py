def main() -> None:
    n, d = map(int, input().split())
    points = [tuple(map(int, input().split())) for _ in range(n)]

    count = 0
    for i in range(n-1):
        for j in range(i+1, n):
            norm = 0
            for yi, zi in zip(points[i], points[j]):
                norm += (yi-zi) ** 2
            if (norm**0.5).is_integer():
                count += 1
    print(count)


if __name__ == '__main__':
    main()
