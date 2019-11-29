def main():
    n, k = map(int, input().split())
    friends = list(map(int, input().split()))

    count = 0

    for friend in friends:
        if friend >= k:
            count += 1

    print(count)


if __name__ == '__main__':
    main()
