def main():
    n = int(input())

    if n < 10:
        print(n)
    elif n < 100:
        print(9)
    elif n < 1000:
        print(n - 90)
    elif n < 10000:
        print(909)
    elif n < 100000:
        print(9 + 900 + (n - 9999))
    else:
        print(90909)


if __name__ == '__main__':
    main()
