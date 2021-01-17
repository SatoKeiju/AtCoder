import collections

def main() -> None:
    n = input()

    c = collections.Counter(n)
    sum_all = sum(map(int, n.split()))
    if sum_all % 3 == 0:
        print(0)
    elif sum_all % 3 == 1:
        if c['1']+c['4']+c['7'] and len(n) >= 2:
            print(1)
        elif c['2']+c['5']+c['8'] >= 2 and len(n) >= 3:
            print(2)
        else:
            print(-1)
    else:
        if c['2']+c['5']+c['8'] and len(n) >= 2:
            print(1)
        elif c['1']+c['4']+c['7'] >= 2 and len(n) >= 3:
            print(2)
        else:
            print(-1)


if __name__ == '__main__':
    main()
