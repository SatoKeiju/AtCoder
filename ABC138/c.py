def main() -> None:
    n = int(input())
    list_ingredients = sorted(list(map(int, input().split())))

    answer = list_ingredients[0]
    for ingredient in list_ingredients[1:]:
        answer = (answer+ingredient) / 2
    print(answer)


if __name__ == '__main__':
    main()
