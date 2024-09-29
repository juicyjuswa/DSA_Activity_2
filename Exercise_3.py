s = int(input("Enter the side length of the square: "))

for i in range(s):
    if i == 0 or i == s - 1:  
        print('x' * s)
    else: 
        print('x' + ' ' * (s - 2) + 'x')