def main() -> None:
    n = int(input())

    songs, times = [], []
    for _ in range(n):
        s, t = input().split()
        songs.append(s)
        times.append(int(t))
    x = input()
    print(sum(times[songs.index(x)+1:]))
    return


if __name__ == '__main__':
    main()
