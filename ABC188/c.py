def main() -> None:
    n = int(input())
    players = list(map(int, input().split()))
    copy_players = players[:]

    for _ in range(n-1):
        players = [max(players[2*i], players[2*i+1]) for i in range(len(players)//2)]
    print(copy_players.index(min(players)) + 1)


if __name__ == '__main__':
    main()
