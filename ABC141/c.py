def main():
    n, k, q = map(int, input().split())

    border = q + 1 - k
    players = [0] * n

    for _ in range(q):
        getter = int(input())
        players[getter-1] += 1

    for player in players:
        print('Yes' if player >= border else 'No')


if __name__ == '__main__':
    main()
