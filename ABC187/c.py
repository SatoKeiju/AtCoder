def main() -> None:
    n = int(input())

    dict_s = {}
    for _ in range(n):
        s = input()
        if s[0] == '!':
            if s[1:] in dict_s:
                print(s[1:])
                return
            else:
                dict_s[s] = True
        else:
            if '!'+s in dict_s:
                print(s)
                return
            else:
                dict_s[s] = 1
    print('satisfiable')


if __name__ == '__main__':
    main()
