def main():
    n, m = map(int, input().split())
    problems = [0 for _ in range(n)]
    was = [0 for _ in range(n)]

    for _ in range(m):
        num, ans = input().split()
        num = int(num) - 1
        if ans == 'AC':
            if problems[num] == 0:
                problems[num] = 1
        else:
            if problems[num] == 0:
                was[num] += 1

    for i, problem in enumerate(problems):
        if problem == 0:
            was[i] = 0

    print('{} {}'.format(sum(problems), sum(was)))


if __name__ == '__main__':
    main()
