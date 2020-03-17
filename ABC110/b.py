def main():
    n, m, x, y = map(int, input().split())

    x_max = max(list(map(int, input().split())) + [x])
    y_min = min(list(map(int, input().split())) + [y])

    print('No War' if x_max <= y_min else 'War')


if __name__ == '__main__':
    main()
