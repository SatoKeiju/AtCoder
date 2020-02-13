def main():
    h = int(input())

    for i in range(50):
        if h < 2**i:
            print(2**i - 1)
            break


if __name__ == '__main__':
    main()
