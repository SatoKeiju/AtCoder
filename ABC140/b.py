def main():
    n = int(input())
    dishes = list(map(int, input().split()))
    points = list(map(int, input().split()))
    adds = list(map(int, input().split()))

    pre = 100
    total = 0
    for dish in dishes:
        if dish == pre + 1:
            total += points[dish-1] + adds[pre-1]
            pre = dish
        else:
            total += points[dish-1]
            pre = dish

    print(total)


if __name__ == '__main__':
    main()
