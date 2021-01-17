def main() -> None:
    a, b = input().split()

    sum_a = int(a[0]) + int(a[1]) + int(a[2])
    sum_b = int(b[0]) + int(b[1]) + int(b[2])

    print(max(sum_a, sum_b))


if __name__ == '__main__':
    main()
