# ACできてない！！

def main():
    from fractions import gcd

    n = int(input())
    num_list = tuple(map(int, input().split()))

    l = 1
    for num in num_list:
        l *= num // gcd(l, num)

    answer = 0

    for num in num_list:
        answer += l // num
        answer %= 10 ** 9 + 7

    print(int(answer))


if __name__ == '__main__':
    main()
