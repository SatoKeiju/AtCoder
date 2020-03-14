def main():
    _ = int(input())
    nums_list = list(map(int, input().split()))

    for num in nums_list:
        if num % 2 == 0 and (num % 3 != 0 and num % 5 != 0):
            print('DENIED')
            return
    else:
        print('APPROVED')


if __name__ == '__main__':
    main()
