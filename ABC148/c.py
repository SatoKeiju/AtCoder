def main():
    from fractions import gcd

    a, b = map(int, input().split())

    print((a * b) // gcd(a, b))


if __name__ == '__main__':
    main()
