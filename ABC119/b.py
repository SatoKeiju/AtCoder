def main():
    n = int(input())

    money = 0
    for _ in range(n):
        num, credit = input().split()
        if credit == 'JPY':
            money += int(num)
        else:
            money += float(num) * 380000.0

    print(money)


if __name__ == '__main__':
    main()
