import matplotlib.pyplot as plt
import numpy as np


def plot_hemisphere(radius):
    # Generate angles from 0 to pi
    angles = np.linspace(0, np.pi, 100)

    # Calculate x and y coordinates of the points on the circumference of the circle
    x = radius * np.cos(angles)
    y = radius * np.sin(angles)

    # Plot the hemisphere
    plt.plot(x, y)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Hemisphere Pattern')
    plt.grid(True)
    plt.show()


# Example usage
radius = 5
plot_hemisphere(radius)
