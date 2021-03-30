def main() -> None:
    n = int(input())
    s = input()

    answer = 0
    for i in range(1, n):
        answer = max(answer, len(set(s[:i])&set(s[i:])))
    print(answer)


if __name__ == '__main__':
    main()
