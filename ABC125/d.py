def main():
    n = int(input())
    numbers = list(map(int, input().split()))

    negs = [num for num in numbers if num <= 0]
    abss = []

    count = 0
    for num in numbers:
        if num >= 0:
            count += num
            abss.append(num)
      else:
          count -= num
          abss.append(-num)

    if len(negs) % 2 == 0:
        print(count)
    else:
        print(count - 2*min(abss))


if __name__ == '__main__':
    main()
