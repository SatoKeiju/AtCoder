def main() -> None:
    s = input()

    print('Yes' if s.replace('hi','') == '' else 'No')
    return


if __name__ == '__main__':
    main()
