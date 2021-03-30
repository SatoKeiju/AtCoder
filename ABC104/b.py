def main() -> None:
    s = input()

    if s[0] == 'A':
        if s[2:-1].count('C') == 1:
            if s[1:].replace('C', '', 1).islower():
                print('AC')
                return
    print('WA')


if __name__ == '__main__':
    main()
