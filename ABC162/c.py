from math import gcd


def main():
    k = int(input())

    answer = 0
    for a in range(1, k+1):
        for b in range(1, k+1):
            for c in range(1, k+1):
                answer += gcd(gcd(a, b), c)

    print(answer)
    return


if __name__ == '__main__':
    main()
