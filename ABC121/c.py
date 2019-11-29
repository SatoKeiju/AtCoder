def main():
    n, m = map(int, input().split())
    shops = sorted([list(map(int, input().split())) for i in range(n)])

    cost = 0
    got = 0
    for shop in shops:
        if got + shop[1] <= m:
            got += shop[1]
            cost += shop[0] * shop[1]
        else:
            cost += (m - got) * shop[0]
            break

    print(cost)


if __name__ == '__main__':
    main()
