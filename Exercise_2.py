size = int(input("Enter the size of the array: "))

elements = list(map(int, input(f"Enter {size} elements separated by space: ").split()))

while len(elements) != size:
    print(f"Error: You need to enter exactly {size} elements.")
    elements = list(map(int, input(f"Enter {size} elements separated by space: ").split()))

for element in elements:
    print(element ** 3)