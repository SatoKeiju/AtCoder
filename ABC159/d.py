def main():
    import collections

    n = int(input())
    balls = list(map(int, input().split()))

    balls_dict = collections.Counter(balls)
    num_patterns = 0
    for value in balls_dict.values():
        num_patterns += value * (value-1) // 2

    for ball in balls:
        print(num_patterns - balls_dict[ball] + 1)


if __name__ == '__main__':
    main()
