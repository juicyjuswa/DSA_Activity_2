def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)
1
result = power(2, 7)
print(f"2^7 = {result}")

result = power(24923742, 0)
print(f"24923742^0 = {result}")