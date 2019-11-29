def main():
    n, m = map(int, input().split())
    foods = set(range(1, m+1))
    for i in range(n):
        opinion = set(list(map(int, input().split()))[1:])
        match = foods & opinion
        if match:
            foods = match
        else:
            foods = set()
            break
    print(len(foods))


if __name__ == '__main__':
    main()
