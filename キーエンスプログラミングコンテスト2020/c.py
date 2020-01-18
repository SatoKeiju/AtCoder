def main():
    n, k, s = map(int, input().split())

    if s == 1e9:
        lst = [s] * k + [1] * (n-k)
    else:
        lst = [s] * k + [s+1] * (n-k)

    print(' '.join(map(str, lst)))


if __name__ == '__main__':
    main()
