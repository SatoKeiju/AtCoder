from fractions import gcd

a, b = map(int, input().split())
ab_gcd = gcd(a, b)

factors = []
while ab_gcd % 2 == 0:
  factors.append(2)
  ab_gcd //= 2
f = 3
while f * f <= ab_gcd:
  if ab_gcd % f == 0:
    factors.append(f)
    ab_gcd //= f
  else:
    f += 2
if ab_gcd != 1:
  factors.append(ab_gcd)

print(len(set(factors)) + 1)
