def main():
    n = int(input())
    a_list = list(map(int, input().split()))

    print('YES' if len(a_list) == len(set(a_list)) else 'NO')


if __name__ == '__main__':
    main()
