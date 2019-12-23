def main():
    s = input()

    cnt = 0
    for a, b in zip(s, s[::-1]):
        if a != b:
            cnt += 1

    print(cnt//2)


if __name__ == '__main__':
    main()
