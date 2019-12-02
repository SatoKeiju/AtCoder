def main():
    x = int(input())

    max_onigiri = x // 100
    mod100 = x % 100
    onigiri = mod100 // 5
    if mod100 % 5 != 0:
        onigiri += 1
    print(1 if onigiri <= max_onigiri else 0)


if __name__ == '__main__':
    main()
