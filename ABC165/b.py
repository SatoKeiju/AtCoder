def main():
    import math

    x = int(input())

    deposit = 100
    for i in range(10000):
        if x <= deposit:
            print(i)
            break
        deposit = math.floor(deposit * 1.01)


if __name__ == '__main__':
    main()
