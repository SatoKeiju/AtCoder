def main():
    import sys
    from operator import itemgetter

    input = sys.stdin.readline
    n = int(input())
    tasks = sorted([list(map(int, input().split())) for _ in range(n)], key=itemgetter(1))

    time = 0
    cando = True
    for task in tasks:
        time += task[0]
        if time > task[1]:
            cando = False

    print('Yes' if cando else 'No')


if __name__ == '__main__':
    main()
