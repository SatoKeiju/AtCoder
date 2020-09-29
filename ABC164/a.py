def main() -> None:
    s, w = map(int, input().split())

    print('unsafe' if s <= w else 'safe')
    return


if __name__ == '__main__':
    main()
