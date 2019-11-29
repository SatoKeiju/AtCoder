def main():
    n = int(input())
    questions = sorted(list(map(int, input().split())))

    half = int(n/2)
    bottom = questions[half-1]
    top = questions[half]

    print(top - bottom)


if __name__ == '__main__':
    main()
