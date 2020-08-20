def main():
    a, b, k = map(int, input().split())

    a, k = max(0, a-k), max(0, k-a)
    b = max(0, b-k)

    print('{} {}'.format(a, b))


if __name__ == '__main__':
    main()
