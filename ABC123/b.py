def main():
    menu = [int(input()) for _ in range(5)]
    mods = [food % 10 if food % 10 != 0 else 10 for food in menu ]
    max_food = mods.index(min(mods))

    times = 0

    for i, food in enumerate(menu):
        if i == max_food or food % 10 == 0:
            times += food
        else:
            times += (food // 10 + 1) * 10

    print(times)


if __name__ == '__main__':
    main()
