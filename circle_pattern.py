import math


def print_circle(radius):
    # Set the center of the circle at (radius, radius)
    center = radius

    # Iterate over each row
    for y in range(2 * radius + 1):
        # Iterate over each column
        for x in range(2 * radius + 1):
            # Calculate distance from the center of the circle
            distance = math.sqrt((x - center) ** 2 + (y - center) ** 2)

            # If the distance is close to the radius, print a character, otherwise print a space
            if abs(distance - radius) < 0.5:
                print("*", end="")
            else:
                print(" ", end="")
        print()  # Move to the next line after each row


# Test the function
radius = int(input("Enter the radius of the circle: "))
print_circle(radius)
