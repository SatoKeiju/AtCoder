def main() -> None:
    n, q = map(int, input().split())
    s = input()

    list_count_ac = [0] * n
    for i in range(1, n):
        if s[i-1:i+1] == 'AC':
            list_count_ac[i] = list_count_ac[i-1] + 1
        else:
            list_count_ac[i] = list_count_ac[i-1]

    for _ in range(q):
        l, r = map(int, input().split())
        print(list_count_ac[r-1] - list_count_ac[l-1])

if __name__ == '__main__':
    main()
