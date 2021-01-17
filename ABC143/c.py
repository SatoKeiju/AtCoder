def main() -> None:
    n = int(input())
    s = input()

    count = 1
    slime_last = s[0]
    for i in range(1, n):
        if s[i] != slime_last:
            count += 1
            slime_last = s[i]
    print(count)


if __name__ == '__main__':
    main()
