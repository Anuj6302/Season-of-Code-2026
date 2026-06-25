# Basic CNN Concept Demonstration

import numpy as np


image = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])


filter = np.array([
    [1, 0],
    [0, -1]
])


print("Input image:")
print(image)

print("\nFilter:")
print(filter)

print("\nCNN uses filters to detect important features from images")
