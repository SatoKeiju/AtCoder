def main():
    s = input()
    t = input()

    count = 0
    for s_x, t_x in zip(s, t):
        if s_x != t_x:
            count += 1

    print(count)


if __name__ == '__main__':
    main()
