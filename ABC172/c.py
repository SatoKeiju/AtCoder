import itertools


def main() -> None:
    n, m, k = map(int, input().split())
    books_a = tuple(map(int, input().split()))
    books_b = tuple(map(int, input().split()))

    accumulate_b = tuple(itertools.accumulate(books_b))

    answer = 0
    idx_current_b = m
    for i, time_a in enumerate(itertools.accumulate(books_a)):
        if time_a <= k:
            answer = max(answer, i+1)
        else:
            break
        for j in reversed(range(idx_current_b)):
            if time_a + accumulate_b[j] <= k:
                answer = max(answer, i+j+2)
                idx_current_b = j + 1
                break
    print(answer)


if __name__ == '__main__':
    main()
