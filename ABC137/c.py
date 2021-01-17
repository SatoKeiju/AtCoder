def main() -> None:
    n = int(input())

    dict_s = {}
    for _ in range(n):
        sorted_s = ''.join(sorted(input()))
        if sorted_s in dict_s:
            dict_s[sorted_s] += 1
        else:
            dict_s[sorted_s] = 1
    answer = 0
    for value in dict_s.values():
        answer += value*(value-1)//2
    print(answer)


if __name__ == '__main__':
    main()
