def main() -> None:
    result = input()

    print('Won' if result[0]==result[1]==result[2] else 'Lost')


if __name__ == '__main__':
    main()
