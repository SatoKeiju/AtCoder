def main():
    import collections

    n, x, y = map(int, input().split())

    distance_list = []
    for i in range(1, n):
        for j in range(i+1, n+1):
            distance_list.append(min(j-i, abs(i-x)+abs(j-y)+1))

    distance_count = collections.Counter(distance_list)
    for i in range(1, n):
        print(distance_count[i])


if __name__ == '__main__':
    main()
