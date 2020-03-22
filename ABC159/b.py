def main():
    s = input()

    n = len(s)
    pre = s[:(n-1)//2]
    suf = s[(n+3)//2-1:]
    print('Yes' if s == s[::-1] and pre == pre[::-1] and suf == suf[::-1] else 'No')


if __name__ == '__main__':
    main()
