def main() -> None:
    a, b = map(int, input().split())

    print(sum(range(b-a+1))-b)


if __name__ == '__main__':
    main()
