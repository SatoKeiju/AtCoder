def main():
  n = int(input())
  t, a = map(int, input().split())
  hs = list(map(int, input().split()))

  temps = [abs(a - (t - h * 0.006)) for h in hs]

  print(temps.index(min(temps)) + 1)


if __name__ == '__main__':
    main()
