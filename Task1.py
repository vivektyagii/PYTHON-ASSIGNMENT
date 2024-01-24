def calculate_area(length, width):
    if length == width:
        return "This is a square"
    else:
        area_of_rectangle = length * width
    return area_of_rectangle

length = int(input("Enter the length:"))
width = int(input("Enter the width:"))
area = calculate_area(length, width)
print(area)