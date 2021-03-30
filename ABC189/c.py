def main() -> None:
    n = int(input())
    oranges = tuple(map(int, input().split()))

    answer = 0
    for l in range(n):
        min_tmp = oranges[l]
        for r in range(l, n):
            min_tmp = min(min_tmp, oranges[r])
            answer = max(answer, min_tmp*(r-l+1))
    print(answer)

if __name__ == '__main__':
    main()
