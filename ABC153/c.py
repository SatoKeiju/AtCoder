def main():
    n, k = map(int, input().split())
    monsters = sorted(list(map(int, input().split())))

    print(sum(monsters[:-k]) if k != 0 else sum(monsters))


if __name__ == '__main__':
    main()
