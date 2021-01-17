def main() -> None:
    n = int(input())
    tuple_a = sorted(tuple(map(int, input().split())), reverse=True)

    answer = 0
    for i in range(n):
        answer += tuple_a[i] * (n-2*i-1)
    print(answer)


if __name__ == '__main__':
    main()
