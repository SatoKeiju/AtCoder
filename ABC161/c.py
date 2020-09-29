def main() -> None:
    n, k = map(int, input().split())

    print(min(n%k, abs(n%k-k)))
    return


if __name__ == '__main__':
    main()
