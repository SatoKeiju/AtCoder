def main():
    s = list(input())

    zerocnt = s.count('0')
    onecnt = len(s) - zerocnt
    if zerocnt <= onecnt:
        print(zerocnt * 2)
    else:
        print(onecnt * 2)


if __name__ == '__main__':
    main()
