def main() -> None:
    sx, sy, gx, gy = map(int, input().split())

    slope = (-gy-sy) / (gx-sx)
    print(sx - (sy/slope))


if __name__ == '__main__':
    main()
