def main():
    people = int(input())

    ways = [int(input()) for _ in range(5)]

    minimum = min(people, min(ways))

    minutes = 5
    if people % minimum == 0:
        minutes += people // minimum - 1
    else:
        minutes += people // minimum

    print(minutes)


if __name__ == '__main__':
    main()
