def main() -> None:
    n = int(input())

    for num_cake in range(n//4+1):
        if (n-num_cake*4) % 7 == 0:
            print('Yes')
            return
    print('No')


if __name__ == '__main__':
    main()
