def digit_sum(num):
    while num >= 10:
        num = sum(int(d) for d in str(num))
    return num

num = int(input("Enter a number: "))
result = digit_sum(num)
print("Final single digit sum:", result)
