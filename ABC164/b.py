def main() -> None:
    a, b, c, d = map(int, input().split())

    if a % d == 0:
        turn_t = a // d
    else:
        turn_t = a // d + 1
    if c % b == 0:
        turn_a = c // b
    else:
        turn_a = c // b + 1
    print('Yes' if turn_a <= turn_t else 'No')
    return


if __name__ == '__main__':
    main()
