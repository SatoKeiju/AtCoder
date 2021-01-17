def main() -> None:
    n = int(input())
    vec_a = tuple(map(int, input().split()))
    vec_b = tuple(map(int, input().split()))

    inner_product = 0
    for a, b in zip(vec_a, vec_b):
        inner_product += a * b
    print('Yes' if inner_product == 0 else 'No')


if __name__ == '__main__':
    main()
