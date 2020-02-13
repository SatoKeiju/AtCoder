def main():
    s, t = input().split()
    a, b = map(int, input().split())
    u = input()

    print('{} {}'.format(a-1, b) if s == u else '{} {}'.format(a, b-1))


if __name__ == '__main__':
    main()
