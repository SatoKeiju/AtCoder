def main():
    from itertools import product

    n, m = map(int, input().split())

    switches = []
    for i in range(m):
        k, *s = map(int, input().split())
        switches.append(s)

    onoffs = list(map(int, input().split()))

    patterns = product([0, 1], repeat=n)
    cnt = 0
    for pattern in patterns:
        for switch, onoff in zip(switches, onoffs):
            switch_ons = 0
            for switch_num in switch:
                if pattern[switch_num-1] == 1:
                    switch_ons += 1
            if switch_ons % 2 != onoff:
                break
        else:
            cnt += 1

    print(cnt)


if __name__ == '__main__':
    main()
