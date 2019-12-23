def main():
    n = int(input())

    if n % 2 != 0:
        print(0)
    else:
        bins = [2 * 5**i for i in range(1, 26)]
        count = 0
        for bin in bins:
            if n < bin:
                break
            else:
                count += n // bin
        print(count)


if __name__ == '__main__':
    main()
