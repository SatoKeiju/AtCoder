def main() -> None:
    k = int(input())

    if k % 2 == 0:
        print(int((k*k) / 4))
    else:
        print(int((k+1)*(k-1) / 4))


if __name__ == '__main__':
    main()
