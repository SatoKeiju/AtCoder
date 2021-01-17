import numpy as np


def main() -> None:
    n = int(input())
    vector = tuple(map(abs, map(int, input().split())))

    print(sum(vector))
    print(np.linalg.norm(vector))
    print(max(vector))


if __name__ == '__main__':
    main()
