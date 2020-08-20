def main():
    n = int(input())
    sticks = sorted(list(map(int, input().split())))

    count = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                l1, l2, l3 = sticks[i], sticks[j], sticks[k]
                if l1 != l2 and l1 != l3 and l2 != l3:
                    if l1 + l2 > l3:
                        count += 1

    print(count)


if __name__ == '__main__':
    main()
