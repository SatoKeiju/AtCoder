def main() -> None:
    h, w = map(int, input().split())

    field = []
    is_black_column = {str(i): False for i in range(w)}
    for _ in range(h):
        line = input()
        if '#' in line:
            for i in range(w):
                if line[i] == '#':
                    is_black_column[str(i)] = True
            field.append(line)
    for line in field:
        answer_line = ''
        for i in range(w):
            if is_black_column[str(i)]:
                answer_line += line[i]
        if answer_line:
            print(answer_line)


if __name__ == '__main__':
    main()
