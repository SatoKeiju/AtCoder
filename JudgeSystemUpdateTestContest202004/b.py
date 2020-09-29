def main() -> None:
    n = int(input())

    balls_red, balls_blue = [], []
    for _ in range(n):
        x, c = input().split()
        if c == 'R':
            balls_red.append(int(x))
        else:
            balls_blue.append(int(x))

    for ball_red in sorted(balls_red):
        print(ball_red)
    for ball_blue in sorted(balls_blue):
        print(ball_blue)
    return


if __name__ == '__main__':
    main()
