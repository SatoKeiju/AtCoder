def main():
    h = int(input())
    w = int(input())
    n = int(input())

    target = max(h, w)
    for i in range(1, min(h, w)+1):
        if target * i >= n:
            print(i)
            break


if __name__ == '__main__':
    main()
