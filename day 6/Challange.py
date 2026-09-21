def power(base, exponent):
    result = 1

    for i in range(exponent):
        result = result * base

    return result


print(power(42, 84))
print(power(42, 168))