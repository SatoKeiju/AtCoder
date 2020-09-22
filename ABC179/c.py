def main() -> None:
    n = int(input())

    count = 0
    for i in range(1, n):
        count += (n-1) // i

    print(count)
    return


if __name__ == '__main__':
    main()
