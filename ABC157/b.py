def main():
    import numpy as np

    card = np.array([list(map(int, input().split())) for _ in range(3)])
    n = int(input())
    for _ in range(n):
        b = int(input())
        card = np.where(card == b, 0, card)

    is_bingo = False
    is_row_bingo = np.sum(card, axis=0).min() == 0
    is_column_bingo = np.sum(card, axis=1).min() == 0
    is_diag_bingo1 = np.sum(np.diag(card)) == 0
    is_diag_bingo2 = np.sum(np.diag(np.fliplr(card))) == 0

    print('Yes' if is_row_bingo or is_column_bingo or is_diag_bingo1 or is_diag_bingo2 else 'No')


if __name__ == '__main__':
    main()
