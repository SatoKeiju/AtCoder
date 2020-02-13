def main():
    h, a = map(int, input().split())

    print(h // a if h % a == 0 else h // a + 1)


if __name__ == '__main__':
    main()
