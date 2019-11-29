def main():
    a, b, c, d = map(int, input().split())

    amount = b - a + 1

    if a % c == 0:
        c_bottom = a // c
    else:
        c_bottom = a // c + 1
    c_top = b // c
    num_c = c_top - c_bottom + 1

    if a % d == 0:
        d_bottom = a // d
    else:
        d_bottom = a // d + 1
    d_top = b // d
    num_d = d_top - d_bottom + 1

    import fractions

    e = int(c * d / fractions.gcd(c, d))
    if a % e == 0:
        e_bottom = a // e
    else:
        e_bottom = a // e + 1
    e_top = b // e
    num_e = e_top - e_bottom + 1

    print(amount - num_c - num_d + num_e)


if __name__ == '__main__':
    main()
