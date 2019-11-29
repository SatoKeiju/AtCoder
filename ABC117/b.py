def main():
    n = int(input())

    sides = list(map(int, input().split()))

    print('Yes' if max(sides) < sum(sides) - max(sides) else 'No')


if __name__ == '__main__':
    main()
