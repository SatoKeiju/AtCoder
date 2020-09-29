from sys import stdin


def main() -> None:
    n = int(input())
    products = set([stdin.readline().replace('\n', '') for _ in range(n)])

    print(len(products))
    return


if __name__ == '__main__':
    main()
