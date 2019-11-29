def main():
    s = int(input())
    a = [s]

    for i in range(1000000):
        n = a[-1]
        fn = 0

        if n % 2 == 0:
            fn = n / 2
        else:
            fn = 3*n + 1

        if fn in a:
            print(i+2)
            break
        else:
            a.append(fn)


if __name__ = '__main__':
    main()
