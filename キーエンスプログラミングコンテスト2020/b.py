def main():
    n = int(input())
    robots = [list(map(int, input().split())) for _ in range(n)]

    min_max = sorted([[list[0] - list[1], sum(list)] for list in robots], key=lambda val: val[1])

    remove = 0
    max_range = -1e9 - 1
    for robot in min_max:
        if max_range <= robot[0]:
            max_range = robot[1]
        else:
            remove += 1

    print(n - remove)


if __name__ == '__main__':
    main()
