n = int(input("Enter an integer: "))
result = ""

if n == 42: result += "a"
if n <= 21: result += "b"
if n % 2 == 0: result += "c"
if n / 2 < 21: result += "d"
if n % 2 != 0 and n >= 45: result += "e"

print(result if result else "f")