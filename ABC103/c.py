def main() -> None:
    n = int(input())
    tuple_a = tuple(map(int, input().split()))

    print(sum(tuple_a) - n)


if __name__ == '__main__':
    main()
