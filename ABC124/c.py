def main():
    s = input()
    l = len(s)

    if len(s) % 2 == 0:
        ideal1 = '01' * int(l / 2)
        ideal2 = '10' * int(l / 2)
    else:
        ideal1 = '01' * (l // 2) + '0'
        ideal2 = '10' * (l // 2) + '1'

    cnt1, cnt2 = 0, 0

    for si, i1i, i2i in zip(s, ideal1, ideal2):
        if si != i1i:
            cnt1 += 1
        if si != i2i:
            cnt2 += 1

    print(min(cnt1, cnt2))


if __name__ == '__main__':
    main()
