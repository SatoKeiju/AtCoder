def main():
    a, b = map(int, input().split())

    if b == 1:
        print(0)
    else:
        total = a
        for i in range(100):
            if total < b:
                total += a - 1
            else:
                print(1 + i)
                break


if __name__ == '__main__':
    main()
