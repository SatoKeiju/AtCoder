def main() -> None:
    a, b, c = map(int, input().split())

    if c:
        print('Takahashi' if a>=b else 'Aoki')
    else:
        print('Takahashi' if a>b else 'Aoki')


if __name__ == '__main__':
    main()
