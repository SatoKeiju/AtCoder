def main():
    w, h, x, y = map(int, input().split())

    area = w * h
    if x * 2 == w and y * 2 == h:
        center = 1
    else:
        center = 0

    print('{} {}'.format(area/2, center))


if __name__ == '__main__':
    main()
