def main():
    s = input()
    former, latter = int(s[:2]), int(s[2:])

    if 1 <= former <= 12 and 1 <= latter <= 12:
        print('AMBIGUOUS')
    elif 1 <= former <= 12 and (latter == 0 or 13 <= latter <= 99):
        print('MMYY')
    elif (former == 0 or 13 <= former <= 99) and 1 <= latter <= 12:
        print('YYMM')
    else:
        print('NA')


if __name__ == '__main__':
    main()
