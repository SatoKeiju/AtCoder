def main():
    n = int(input())
    monsters = list(map(int, input().split()))
    heroes = list(map(int, input().split()))

    cnt = 0
    for i in range(n):
        if heroes[i] <= monsters[i]:
            cnt += heroes[i]
        else:
          cnt += monsters[i]
          heroes[i] -= monsters[i]
          if heroes[i] <= monsters[i+1]:
              cnt += heroes[i]
              monsters[i+1] -= heroes[i]
          else:
              cnt += monsters[i+1]
              monsters[i+1] = 0

    print(cnt)


if __name__ = '__main__':
    main()
