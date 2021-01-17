def main() -> None:
    n = int(input())

    difference = 0
    list_difference = []
    for _ in range(n):
        a, b = map(int, input().split())
        difference -= a
        list_difference.append(2*a + b)
    list_difference.sort()
    count = 0
    while difference <= 0:
        difference += list_difference.pop()
        count += 1

    print(count)


if __name__ == '__main__':
    main()
