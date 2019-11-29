def main():
    num_x, num_y, num_z, k = map(int, input().split())

    x_list = sorted(list(map(int, input().split())))
    y_list = sorted(list(map(int, input().split())))
    z_list = sorted(list(map(int, input().split())))

    xy_list = sorted([x + y for x in x_list for y in y_list], reverse=True)[:k]
    xyz_list = sorted([xy + z for xy in xy_list for z in z_list], reverse=True)[:k]

    for xyz in xyz_list:
        print(xyz)


if __name__ == '__main__':
    main()
