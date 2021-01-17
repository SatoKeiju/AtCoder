def main() -> None:
    n = int(input())
    cities = [tuple(map(int, input().split())) for _ in range(n)]

    distances = []
    for i in range(n-1):
        for j in range(i+1, n):
            x1, y1 = cities[i]
            x2, y2 = cities[j]
            distances.append(((x2-x1)**2+(y2-y1)**2)**0.5)
    print(2*sum(distances) / n)


if __name__ == '__main__':
    main()
