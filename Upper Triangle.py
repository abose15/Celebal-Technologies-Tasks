def upper_triangular(n):
    for i in range(n, 0, -1):
        print('* ' * i)

n = int(input("Enter the layer of the triangle. "))
upper_triangular(n)
