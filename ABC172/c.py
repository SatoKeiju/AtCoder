def main():
    n, m, k = map(int, input().split())
    a_books = list(map(int, input().split()))
    b_books = list(map(int, input().split()))

    total = 0
    for i, a_book in enumerate(a_books):
        if total + a_book <= k:
            total += a_book
            a_books[i] = total
        else:
            a_books = a_books[:i]
            break
            
    answer = 0
    for i, a_time in enumerate(a_books):
        time_left = k - a_time
        if time_left < 0:
            break
        elif time_left == 0:
            answer = max(answer, i+1)
            break
        else:
            for j, b_book in enumerate(b_books):
                if time_left < b_book:
                    answer = max(answer, i+1+j)
                    break
                else:
                    time_left -= b_book
            else:
                answer = max(answer, i+1+m)

    print(answer)


if __name__ == '__main__':
    main()
