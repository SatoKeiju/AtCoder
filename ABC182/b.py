def main() -> None:
    n = int(input())
    tuple_num = tuple(map(int, input().split()))

    answer = min(tuple_num)
    gcd_temp_max = 1
    for k in range(2, max(tuple_num)+1):
        gcd_temp = 0
        for num in tuple_num:
            if num % k == 0:
                gcd_temp += 1
        if gcd_temp_max <= gcd_temp:
            answer = k
            gcd_temp_max = gcd_temp
    print(answer)


if __name__ == '__main__':
    main()
