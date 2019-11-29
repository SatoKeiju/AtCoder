def main():
    s = input()

    length, ans = 0, 0
    for cha in s:
        if cha in 'ACGT':
            length += 1
            ans = max(ans, length)
        else:
            length = 0

    print(ans)


if __name__ == '__main__':
    main()
