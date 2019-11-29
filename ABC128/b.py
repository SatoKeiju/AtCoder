def main():
    from operator import itemgetter

    n = int(input())

    restaurants = []
    for i in range(n):
        name, score = input().split()
        restaurants.append([name, -int(score), i+1])

    for restaurant in sorted(restaurants, key=itemgetter(0, 1)):
        print(restaurant[2])


if __name__ == '__main__':
    main()
