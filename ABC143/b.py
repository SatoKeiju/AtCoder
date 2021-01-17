def main() -> None:
    n = int(input())
    takoyakis = tuple(map(int, input().split()))

    answer = 0
    for i in range(n-1):
        for j in range(i+1, n):
            answer += takoyakis[i] * takoyakis[j]
    print(answer)


if __name__ == '__main__':
    main()
