start = int(input("Enter start number: "))
stop = int(input("Enter stop number: "))

odd_sum = 0
for num in range(start, stop + 1):
    if num % 2 != 0:
        odd_sum += num

print("Sum of odd numbers:", odd_sum)
