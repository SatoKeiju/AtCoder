def main() -> None:
    n, k = map(int, input().split())
    tuple_a = tuple(map(int, input().split()))

    answer = (n-1) // (k-1)
    if (n-1) % (k-1) == 0:
        print(answer)
    else:
        print(answer + 1)


if __name__ == '__main__':
    main()
