import collections


def main() -> None:
    n = input()

    s_n = 0
    c = collections.Counter(n)
    for key, value in c.items():
        s_n += int(key) * value
    print('Yes' if int(n)%s_n==0 else 'No')


if __name__ == '__main__':
    main()
