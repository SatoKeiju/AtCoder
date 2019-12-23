def main():
    n = int(input())
    bricks = list(map(int, input().split()))

    count = 0
    num = 1
    for brick in bricks:
        if brick != num:
            count += 1
        else:
            num += 1

    print(count if count != len(bricks) else -1)


if __name__ == '__main__':
    main()
