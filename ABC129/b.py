def main():
    n = int(input())
    weights = list(map(int, input().split()))

    diff = sum(weights)
    for i in range(n):
        if abs(sum(weights[:i]) - sum(weights[i:])) < diff:
            diff = abs(sum(weights[:i]) - sum(weights[i:]))

    print(diff)


if __name__ = '__main__':
    main()
