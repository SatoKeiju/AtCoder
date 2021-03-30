def main() -> None:
    s = input()
    k = int(input())

    if s[:min(k-1, len(s))] == '1'*min(k-1, len(s)):
        print(s[min(k-1, len(s)-1)])
    else:
        for num in s:
            if num != '1':
                print(num)
                return


if __name__ =='__main__':
    main()
