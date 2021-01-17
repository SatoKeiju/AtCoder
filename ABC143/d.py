def main() -> None:
    n = int(input())
    lods = sorted(tuple(map(int, input().split())))

    count = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            idx_l = j
            idx_r = len(lods)
            while idx_r-idx_l > 1:
                idx_mid = (idx_l+idx_r) // 2
                if lods[idx_mid] < lods[i]+lods[j]:
                    idx_l = idx_mid
                else:
                    idx_r = idx_mid
            count += idx_l - j
    print(count)


if __name__ == '__main__':
    main()
