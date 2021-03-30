def main() -> None:
    tuple_a = sorted(tuple(map(int, input().split())))

    print(tuple_a[2] - tuple_a[0])


if __name__ == '__main__':
    main()
