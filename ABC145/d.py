def combination(n: int, r: int) -> int:
    r = min(r, n-r)
    if r == 0:
        return 1
    if r == 1:
        return n
    numerator = [n-r+i+1 for i in range(r)]
    denominator = [i+1 for i in range(r)]
    for p in range(2, r+1):
        pivot = denominator[p-1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1, r, p):
                numerator[k-offset] /= pivot
                denominator[k] /= pivot
    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result


def main() -> None:
    x, y = map(int, input().split())

    if (x+y) % 3 != 0:
        print(0)
        return
    n = (2*y-x) // 3
    m = (2*x-y) // 3
    if n < 0 or m < 0:
        print(0)
        return
    print(combination(n+m, n) % 1000000007)


if __name__ == '__main__':
    main()
