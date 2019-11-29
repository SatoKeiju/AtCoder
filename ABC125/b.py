def main():
    _ = int(input())

    prices = list(input().split())
    costs = list(input().split())

    benefit = 0
    for price, cost in zip(prices, costs):
        if int(price) > int(cost):
            benefit += int(price) - int(cost)

    print(benefit)


if __name__ == '__main__':
    main()
