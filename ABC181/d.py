import collections
import itertools


def main() -> None:
    s = input()

    if len(s) <= 2:
        print('Yes' if int(s)%8 == 0 or int(s[::-1])%8 == 0 else 'No')
        return
    c = collections.Counter(s)
    memo_num = ''
    for num, count in c.items():
        memo_num += num * min(count, 3)
    for num_str in itertools.permutations(memo_num, 3):
        if int(''.join(num_str)) % 8 == 0:
            print('Yes')
            return
    print('No')


if __name__ == '__main__':
    main()
