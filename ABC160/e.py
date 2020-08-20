def main():
    x, y, a, b, c = map(int, input().split())
    red_apples = sorted(list(map(int, input().split())), reverse=True)[:x]
    green_apples = sorted(list(map(int, input().split())), reverse=True)[:y]
    colorless_apples = sorted(list(map(int, input().split())), reverse=True)[:min(x+y, c)]

    print(sum(sorted(red_apples + green_apples + colorless_apples, reverse=True)[:x+y]))


if __name__ == '__main__':
    main()
