import math
 
# Square
# Ask for the information
side = float(input("Enter the length of the side of the square: "))

# Calculate the area
area = side * side

# Display the area
print(f"The area of the square is: {area:.2f}")

# Rectangle
# Ask for the information
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate the area
area = length * width

# Display the area
print(f"The area of the rectangle is: {area:.2f}")

# Circle
# Ask for the information
radius = float(input("Enter the radius of the circle: "))

# Calculate the area
area = math.pi * radius * radius

# Display the area
print(f"The area of the circle is: {area:.2f}")

# Square
# Ask for the information
side_cm = float(input("Enter length of the side of the square (in cm): "))

# Calculate the area
area_cm2 = side_cm * side_cm

# Display the area
print(f"The area of the square is: {area_cm2:.2f} cm²")

area_m2 = area_cm2 / 10000
print(f"The area of the square is: {area_m2:.4f} m²")

# Rectangle
# Ask for the information
length_cm = float(input("Enter the length of the rectangle (in cm): "))
width_cm = float(input("Enter the width of the rectangle (in cm): "))

# Calculate the area
area_cm2 = length_cm * width_cm

# Display the area
print(f"The area of the rectangle is: {area_cm2:.2f} cm²")

area_m2 = area_cm2 / 10000
print(f"The area of the rectangle is: {area_m2:.4f} m²")

# Circle
# Ask for the information
radius_cm = float(input("Enter the radius of the circle (in cm): "))

# Calculate the area
area_cm2 = math.pi * radius_cm * radius_cm

# display the area
print(f"The area of the circle is: {area_cm2:.2f} cm²")

area_m2 = area_cm2 / 10000
print(f"The area of the circle is: {area_m2:.4f} m²")

