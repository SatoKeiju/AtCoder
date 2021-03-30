def main() -> None:
    h, w = map(int, input().split())
    field = ['.' * (w+2)]

    for _ in range(h):
        field.append('.' + input() + '.')
    field.append('.' * (w+2))

    for i in range(1, h+1):
        for j in range(1, w+1):
            area = field[i][j]
            if area == '#':
                sides = [
                    field[i-1][j],
                    field[i+1][j],
                    field[i][j-1],
                    field[i][j+1]
                ]
                if not '#' in sides:
                    print('No')
                    return
    print('Yes')


if __name__ == '__main__':
    main()
