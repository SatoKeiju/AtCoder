def main() -> None:
    n, m = map(int, input().split())
    favors = [tuple(map(int, input().split())) for _ in range(m)]

    favors = sorted(favors, key=lambda x: x[1])
    brigde_last = 0
    answer = 0
    for favor in favors:
        if favor[0] <= brigde_last:
            continue
        else:
            brigde_last = favor[1] - 1
            answer += 1
    print(answer)


if __name__ == '__main__':
    main()
