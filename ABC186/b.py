import numpy as np


def main() -> None:
    h, w = map(int, input().split())

    grid = np.array([tuple(map(int, input().split())) for _ in range(h)])
    num_min = grid.min()
    print((grid-num_min).sum())


if __name__ == '__main__':
    main()
