def main():
    a, b, c = map(int, input().split())

    print('Yes' if a + b < c and 4 * a * b < (c - a - b) ** 2 else 'No')


if __name__ == '__main__':
    main()
