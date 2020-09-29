def main() -> None:
    a, b, m = map(int, input().split())
    refrigerators = tuple(map(int, input().split()))
    microwaves = tuple(map(int, input().split()))

    answer = min(refrigerators) + min(microwaves)
    for _ in range(m):
        x, y, c = map(int, input().split())
        answer = min(answer, refrigerators[x-1]+microwaves[y-1]-c)

    print(answer)
    return


if __name__ == '__main__':
    main()
