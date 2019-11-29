def main():
    s = input()

    for i in range(len(s)):
        if i % 2 == 0 and s[i] == 'L':
            print('No')
            break
        if i % 2 == 1 and s[i] =='R':
            print('No')
            break
    else:
        print('Yes')


if __name__ == '__main__':
    main()
