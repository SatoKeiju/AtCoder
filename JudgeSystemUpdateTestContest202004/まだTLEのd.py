from math import gcd


def main() -> None:
    n, q = map(int, input().split())
    a_list = list(map(int, input().split()))
    s_tuple = tuple(map(int, input().split()))

    for i in range(1, n):
        a_list[i] = gcd(a_list[i-1], a_list[i])
        a_set = set(a_list)
    for s in s_tuple:
        for a in sorted(list(a_set), reverse=True):
            if gcd(s, a) == 1:
                print(a_list.index(a) + 1)
                break
        else:
            print(gcd(s, a_list[-1]))

    return


if __name__ == '__main__':
    main()
