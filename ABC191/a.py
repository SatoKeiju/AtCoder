def main() -> None:
    v, t, s, d = map(int, input().split())

    print('No' if v*t<=d<=v*s else 'Yes')


if __name__ == '__main__':
    main()
