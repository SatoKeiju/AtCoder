def main() -> None:
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))

    eaten = [0] * m
    for i in range(n):
        x_list = list(map(int, input().split()))
        for j, x in enumerate(x_list):
            eaten[j] += x

    for i, a in enumerate(a_list):
        if eaten[i] < a:
            print('No')
            return

    print('Yes')
    return


if __name__ == '__main__':
    main()
