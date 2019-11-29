def main():
    a, b = map(int, input().split())

    a, b = min(a, b), max(a, b)
    sum1 = b
    sum2 = max(a, b-1)
    print(sum1 + sum2)


if __name__ == '__main__':
    main()
