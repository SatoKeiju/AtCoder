def main():
    r, d, x = map(int, input().split())

    for i in range(10):
        print(r * x - d)
        x = r * x - d


if __name__ == '__main__':
    main()
