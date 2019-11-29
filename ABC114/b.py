def main():
    s = input()

    dif = 753
    for i in range(len(s)-2):
        dif = min(dif, abs(753-int(s[i:i+3])))

    print(dif)



if __name__ == '__main__':
    main()
