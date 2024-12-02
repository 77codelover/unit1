ch = 0
while ch!=5:
    print("1 . Area of Circle:");
    print("2 . Area of Square & Rectangle:")
    print("3 . Area of Triangle:")
    print("4 . Simple Interest:")
    print("5 . Exit")
    ch = int(input("Enter your Choice: "))
    if ch == 1:
        #circle = 3.14*r*r
        c = float(input("Enter the Radius of circle: "))
        area_circle = 3.14 * c * c
        print("Area of circle is: ", area_circle)
    elif ch ==2:
        #Square = l * l & Rectangle = l * b
        l = int(input("Enter the Length of the square & rectangle : "))
        b = int(input("Enter the Breadth of the rectangle : "))
        area_sqr = l * l
        area_rect = l * b
        print("Area of Square : ",area_sqr)
        print("Area of Rectangle : ",area_rect)
    elif ch==3:
        #Triangle = (a+b+c)/2
        a = int(input("Enter the first side of the triangle : "));
        b = int(input("Enter the second side of the triangle : "));
        c = int(input("Enter the third side of the triangle : "));
        area_triangle = (a + b + c) / 2
        print("Area of Triangle : ", area_triangle)
    elif ch==4:
        #circle = 3.14*r*r
        c = float(input("Enter the Radius of circle: "))
        area_circle = 3.14 * c * c
        print("Area of circle is: ", area_circle)
    elif ch == 5:
        print("Thank you ")
    else:
        print("Invalid choice")









