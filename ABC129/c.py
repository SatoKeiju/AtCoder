    n, m = map(int, input().split())
    broken = [int(input()) for _ in range(m)]

    ways = [1] * (n+1)
    for i in broken:
        ways[i] = 0

    keep = 1
    for i in range(1, n+1):
        if ways[i]:
            if keep == 2:
                ways[i] = ways[i-1] + ways[i-2]
            elif keep == 1:
                ways[i] = ways[i-1]
                keep += 1
            else:
                ways[i] = ways[i-2]
                keep += 1
        else:
            keep = 0

    print(ways[-1] % 1000000007)
