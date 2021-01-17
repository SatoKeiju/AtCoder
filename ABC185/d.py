def main() -> None:
    n, m = map(int, input().split())
    tuple_a = sorted(tuple(map(int, input().split())))

    if n == m:
        print(0)
        return
    elif m == 0:
        print(1)
        return

    blue_last = 0
    list_white_length = []
    for a in tuple_a:
        if a - blue_last > 1:
            list_white_length.append(a-blue_last-1)
        blue_last = a
    if tuple_a[-1] != n:
        list_white_length.append(n-blue_last)
    stamp = min(list_white_length)

    answer = 0
    for length in list_white_length:
        if length % stamp == 0:
            answer += length // stamp
        else:
            answer += length//stamp + 1
    print(answer)


if __name__ == '__main__':
    main()
