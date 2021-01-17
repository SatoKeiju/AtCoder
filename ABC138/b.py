def main() -> None:
    n = int(input())
    tuple_a = tuple(map(int, input().split()))

    answer_inverse = 0
    for a in tuple_a:
        answer_inverse += 1 / a
    print(1 / answer_inverse)


if __name__ == '__main__':
    main()
