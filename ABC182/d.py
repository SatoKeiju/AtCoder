def main() -> None:
    n = int(input())
    tuple_a = tuple(map(int, input().split()))

    cumulative_sum = 0
    cumulative_max_last = 0
    current = 0
    answer = 0
    for a in tuple_a:
        cumulative_sum += a
        if cumulative_max_last < cumulative_sum:
            cumulative_max_last = cumulative_sum
        if current + cumulative_max_last > answer:
            answer = current + cumulative_max_last
        current += cumulative_sum
    print(answer)


if __name__ == '__main__':
    main()
