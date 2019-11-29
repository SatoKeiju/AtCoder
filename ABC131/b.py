def main():
    n, l = map(int, input().split())

    apples = [l + i for i in range(n)]

    if 0 in apples:
        print(sum(apples))
    elif apples[0] > 0:
        print(sum(apples[1:]))
    else:
        print(sum(apples[:-1]))


if __name__ == '__main__':
    main()
