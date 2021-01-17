def main() -> None:
    n, m, t = map(int, input().split())

    battery_current = n
    time_left = 0
    for _ in range(m):
        a, b = map(int, input().split())
        if battery_current - (a-time_left) <= 0:
            print('No')
            return
        battery_current -= a - time_left
        time_cafe = b - a
        battery_current = min(n, battery_current+time_cafe)
        time_left = b
    print('Yes' if t-time_left < battery_current else 'No')


if __name__ == '__main__':
    main()
