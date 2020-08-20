def main():
    k = int(input())
    a, b = map(int, input().split())

    is_ok = False
    for i in range(a, b+1):
        if i % k == 0:
            is_ok = True
            break

    print('OK' if is_ok else 'NG')


if __name__ == '__main__':
    main()
