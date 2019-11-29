def main():
    s = sorted(list(input()))

    if (s[0] == s[1] and s[0] != s[2]) and s[2] == s[3]:
      print('Yes')
    else:
      print('No')


if __name__ == '__main__':
    main()
