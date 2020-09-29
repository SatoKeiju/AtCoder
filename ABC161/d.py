from collections import deque


def main() -> None:
    k = int(input())

    d = deque(range(1, 10))
    for _ in range(k):
        num = d.popleft()
        if num % 10 != 0:
            d.append(num*10 + (num%10-1))
        d.append(num*10 + num%10)
        if num % 10 != 9:
            d.append(num*10 + (num%10+1))

    print(num)
    return


if __name__ == '__main__':
    main()
