def main() -> None:
    s, l, r = map(int, input().split())

    if l <= s <= r:
        print(s)
    elif s < l:
        print(l)
    else:
        print(r)
        
    return


if __name__ == '__main__':
    main()
