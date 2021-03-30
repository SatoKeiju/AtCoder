def main() -> None:
    n = int(input())
    tuple_a = sorted(tuple(map(int, input().split())))

    print(tuple_a[-1] - tuple_a[0])


if __name__ == '__main__':
    main()
