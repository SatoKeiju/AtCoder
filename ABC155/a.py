def main():
    nums_set = set(map(int, input().split()))

    print('Yes' if len(nums_set) == 2 else 'No')


if __name__ == '__main__':
    main()
