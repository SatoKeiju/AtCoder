def main():
    n = int(input())
    h = list(map(int, input().split()))
    h = [0] + h

    is_able = True
    for i in range(n):
        if h[i] < h[i+1]:
            h[i+1] -= 1
        elif h[i] == h[i+1]:
            pass
        else:
            is_able = False
            break

    print('Yes' if is_able else 'No')


if __name__ == '__main__':
    main()
