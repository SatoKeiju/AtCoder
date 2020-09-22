def main() -> None:
    n, k = map(int, input().split())
    cities = tuple(map(int, input().split()))

    check = [1] + [0] * (n-1)
    city_next = cities[0] - 1
    for i in range(1, n+1):
        if check[city_next] == 0:
            check[city_next] = i + 1
            city_next = cities[city_next] - 1
        else:
            to_loop = check[city_next] - 1
            length_loop = i - check[city_next] + 1
            break

    k_left = (k-to_loop) % length_loop
    for _ in range(k_left):
        city_next = cities[city_next] - 1

    print(city_next + 1)
    return


if __name__ == '__main__':
    main()
