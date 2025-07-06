a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

def find_lcm(x, y):
    greater = max(x, y)
    while True:
        if greater % x == 0 and greater % y == 0:
            return greater
        greater += 1

lcm = find_lcm(a, b)
print(f"LCM of {a} and {b} is: {lcm}")
