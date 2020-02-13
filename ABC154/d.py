def calc_e(num):
    return (num + 1) / 2

def main():
    n, k = map(int, input().split())
    dices = list(map(int, input().split()))

    current = (sum(dices[:k]) + k) / 2
    e_max = (sum(dices[:k]) + k) / 2
    for i in range(n-k):
        current = current + calc_e(dices[i+k]) - calc_e(dices[i])
        e_max = max(e_max, current)

    print(e_max)


if __name__ == '__main__':
    main()
