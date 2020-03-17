def main():
    n = int(input())
    start_word = input()

    used_words = [start_word]
    result = 'Yes'
    for _ in range(n-1):
        word = input()
        if used_words[-1][-1] == word[0] and word not in used_words:
            used_words.append(word)
        else:
            result = 'No'
            break

    print(result)


if __name__ == '__main__':
    main()
