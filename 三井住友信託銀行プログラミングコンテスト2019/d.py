def main():
    import itertools
    import re

    n = int(input())
    s = input()

    cnt = 0
    for key in itertools.product('0123456789', repeat=3):
        key1, key2, key3 = map(str, key)
        if key1 in s:
            key1_idx = s.find(key1)
            if key2 in s[key1_idx+1:]:
                key2_idx = key1_idx + s[key1_idx+1:].find(key2) + 1
                if key3 in s[key2_idx+1:]:
                    cnt += 1

    print(cnt)


if __name__ == '__main__':
    main()
