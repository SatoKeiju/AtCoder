def main():
    n, m = map(int, input().split())
    homeworks = tuple(map(int, input().split()))

    print(max(-1, n - sum(homeworks)))
    return


if __name__ == '__main__':
    main()
