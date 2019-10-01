n = int(input())
counts = list(map(int, input().split()))

order = [0] * n
for i, count in enumerate(counts):
  order[count-1] = i+1

print(' '.join(map(str, order)))
