def main() -> None:
    n = int(input())
    s = input()

    w_left = 0
    e_right = s.count('E')
    answer = n
    for i in range(n):
        if s[i] == 'E':
            e_right -= 1
        count = w_left + e_right
        answer = min(answer, count)
        if s[i] == 'W':
            w_left += 1
    print(answer)


if __name__ == '__main__':
    main()
