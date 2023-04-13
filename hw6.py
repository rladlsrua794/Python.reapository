def display_multiplication_table(n, k) :
    for i in range(1, 10, 1) :
        for j in range (n, k, 1) :
            print(f'{j} x {i} = {j * i:2d}\t', end = '')
        print()
    print()

display_multiplication_table(2, 6)
display_multiplication_table(6, 10)
