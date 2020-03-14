def main():
    h, w = map(int, input().split())

    if h == 1 or w == 1:
        print(1)
    else:
        print((w * h + 1) // 2)


if __name__ == '__main__':
    main()
