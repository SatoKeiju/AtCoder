def main():
    h, _ = map(int, input().split())
    specials = list(map(int, input().split()))

    print('Yes' if h <= sum(specials) else 'No')


if __name__ == '__main__':
    main()
