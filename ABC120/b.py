def main():
    a, b, k = map(int, input().split())
    a, b = min(a, b), max(a, b)

    lst = []
    for i in range(1, a+1):
        if a % i == 0:
            lst.append(i)
    lst.sort(reverse=True)
    cnt = 0
    for num in lst:
        if b % num == 0:
            cnt += 1
            if cnt == k:
                print(num)
                break


if __name__ == '__main__':
    main()
