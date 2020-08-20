def main():
    from itertools import combinations_with_replacement
    n, m, q = map(int, input().split())
    requirements = [list(map(int, input().split())) for _ in range(q)]

    score_max = 0
    for a in combinations_with_replacement(range(1, m+1), n):
        score = 0
        for requirement in requirements:
            if a[requirement[1]-1] - a[requirement[0]-1] == requirement[2]:
                score += requirement[3]
        score_max = max(score, score_max)

    print(score_max)


if __name__ == '__main__':
    main()
