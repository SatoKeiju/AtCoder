import collections


def main() -> None:
    n = int(input())
    boss_dict = collections.Counter(tuple(map(int, input().split())))

    for i in range(n):
        print(boss_dict[i+1] if boss_dict[i+1] else 0)

    return


if __name__ == '__main__':
    main()
