import math


def main() -> None:
    a, b, x = map(int, input().split())

    if a*a*b/2 < x:
        print(math.degrees(math.atan(2*b/a - 2*x/a/a/a)))
    else:
        print(math.degrees(math.atan(a*b*b/2/x)))


if __name__ == '__main__':
    main()
