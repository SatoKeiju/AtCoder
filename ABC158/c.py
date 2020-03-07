def main():
    import math
    a, b = map(int, input().split())

    for i in range(10100):
        if math.floor(i * 0.08) == a and math.floor(i * 0.1) == b:
            print(i)
            break
    else:
        print(-1)


if __name__ == '__main__':
    main()
