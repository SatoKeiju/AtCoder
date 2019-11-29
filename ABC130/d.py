def main():
    n, k = map(int, input().split())
    numbers = list(map(int, input().split()))

    cnt = 0
    right = 0
    s = 0
    for i in range(n):
        while s < k:
            if right == n:
                break
            else:
                s += numbers[right]
                right += 1
        if s < k:
            break
        cnt += n - right + 1
        s -= numbers[i]

    print(cnt)


if __name__ == '__main__':
    main()
