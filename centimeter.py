centimeter = int(input("Enter the centimeter:"))
inches = centimeter/2.54
if centimeter < 0:
    print("Invalid input")
else:
    print(f"The Length of {centimeter} centimeter = {inches} inches:" )