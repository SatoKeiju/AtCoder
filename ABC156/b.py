def main():
    n, k = map(int, input().split())

    for i in range(100):
        if k ** i <= n:
            continue
        else:
            print(i)
            return


if __name__ == '__main__':
    main()
