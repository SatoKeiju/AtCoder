def main() -> None:
    x = int(input())

    list_exp = [1]
    for i in range(2, int(x**0.5)+1):
        exp = i
        while True:
            if exp <= x:
                list_exp.append(exp)
                exp *= i
            else:
                break
    print(max(list_exp))


if __name__ == '__main__':
    main()
