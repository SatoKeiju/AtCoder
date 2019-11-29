def main():
    s = input()

    status = True
    for i in range(3):
        if s[i] == s[i + 1]:
            status = False

    print('Good' if status else 'Bad')


if __name__ == '__main__':
    main()
