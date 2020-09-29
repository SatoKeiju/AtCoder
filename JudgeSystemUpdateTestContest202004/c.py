def count_blocks(x: int, y: int, z: int) -> int:
    if x<y or y<z or z<0:
        return 0
    if x==0 and y==0 and z==0:
        return 1
    return count_blocks(x-1,y,z) + count_blocks(x,y-1,z) + count_blocks(x,y,z-1)


def main() -> None:
    a1, a2, a3 = map(int, input().split())

    print(count_blocks(a1, a2, a3))
    return


if __name__ == '__main__':
    main()
