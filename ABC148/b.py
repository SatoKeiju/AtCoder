def main():
    n = int(input())
    s, t = input().split()

    word = ''
    for a, b in zip(s, t):
      word += a + b

    print(word)


if __name__ == '__main__':
    main()
