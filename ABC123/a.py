def main():
    input_list = [int(input()) for _ in range(6)]

    poles = input_list[:-1]
    k = input_list[-1]

    if poles[-1] - poles[0] > k:
        print(':(')
    else:
        print('Yay!')


if __name__ == '__main__':
    main()
