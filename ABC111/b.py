def main():
    n = int(input())

    print(n if n % 111 == 0 else (n // 111 + 1) * 111)


if __name__ == '__main__':
    main()
