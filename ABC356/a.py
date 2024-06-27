def main() -> None:
    n,l,r = map(int, input().split())
    answer = [i+1 for i in range(n)]
    answer[l-1:r] = reversed(answer[l-1:r])
    print(*answer)


if __name__ == '__main__':
    main()
