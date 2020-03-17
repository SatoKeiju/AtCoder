def main():
    n, t = map(int, input().split())

    min_cost = 1001
    for _ in range(n):
        ci, ti = map(int, input().split())
        if ti <= t and ci < min_cost:
            min_cost = ci

    print('TLE' if min_cost == 1001 else min_cost)


if __name__ == '__main__':
    main()
