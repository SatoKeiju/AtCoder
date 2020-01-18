def main():
    import itertools

    n = int(input())
    ps = tuple(map(int, input().split()))
    qs = tuple(map(int, input().split()))

    num_list = list(itertools.permutations([i for i in range(1, n+1)]))

    print(abs(num_list.index(ps) - num_list.index(qs)))


if __name__ == '__main__':
    main()
