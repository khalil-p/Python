from ast import Return


row = int(input("Enter the number of rows : "))


def half_triangle(row):
    for i in range(row):
        print("* "*(row-i) + " "*i)


half_triangle(3)
