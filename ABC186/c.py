def main() -> None:
    n = int(input())

    answer = 0
    for i in range(1, n+1):
        if '7' not in str(i)+oct(i):
            answer += 1
    print(answer)


if __name__ == '__main__':
    main()
