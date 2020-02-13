def main():
    n = int(input())

    table = [0] * 100
    for i in range(n):
        i_str = str(i)
        table[int(i_str[0]) * 10 + int(i_str[-1])] += 1

    num = 0
    for i in range(1, 10):
        for j in range(1, 10):
            num += table[i*10 + j] * table[j*10 + i]

    print(num)


if __name__ == '__main__':
    main()
