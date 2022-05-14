def raise_in_power(base, power):
    result = 1
    for i in range(power):
        result = result * base
    print(result)

raise_in_power(4, 2)