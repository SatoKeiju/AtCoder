def main() -> None:
    a, b = map(int, input().split())

    print(a if a<=b else a-1)


if __name__ == '__main__':
    main()
