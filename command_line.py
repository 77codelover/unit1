min = int(input("Enter the minimum number: "))
max = int(input("Enter the maximum number: "))

even = 0
odd = 0

for number in range(min,max + 1):
    if number % 2 == 0:
        even = even + number
    else:
        odd = odd + number

print("Sum of Even numbers : ",even)
print("Sum of Odd numbers : ",odd)