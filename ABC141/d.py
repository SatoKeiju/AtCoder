def main():
    import heapq as hq

    n, m = map(int, input().split())
    a = [-int(i) for i in input().split()]
    hq.heapify(a)

    for _ in range(m):
        hq.heappush(a, -(-hq.heappop(a) // 2))

    print(sum(a) * -1)


if __name__ == '__main__':
    main()
