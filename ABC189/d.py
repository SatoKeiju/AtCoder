def main() -> None:
    n = int(input())

    count_true, count_false = 1, 1
    for _ in range(n):
        s = input()
        if s == 'AND':
            count_false += count_true + count_false
        else:
            count_true += count_true + count_false
    print(count_true)


if __name__ == '__main__':
    main()
