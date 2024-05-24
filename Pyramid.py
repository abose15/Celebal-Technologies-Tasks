def pyramid(n):
    for i in range(1, n + 1):
        print(' ' * (n - i) + '* ' * i)

n = int(input("Enter the layer of the pyramid. "))
pyramid(n)
