def main():
    num_dict = {'1': '9', '9': '1'}
    num = input()
    print(''.join(num_dict[c] for c in num))


if __name__ == '__main__':
    main()
