def main():
    import copy

    n = int(input())

    chars_list = ['a']
    a = 'abcdefghij'

    while n - 1 > 0:
        new_list = []
        for char in chars_list:
            for alphabet in a:
                new_list.append(char + alphabet)
                if alphabet not in char:
                    break
        chars_list = copy.deepcopy(new_list)
        n -= 1

    print('\n'.join(chars_list))

if __name__ == '__main__':
    main()
