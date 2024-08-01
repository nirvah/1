import numpy as np
import cv2

# Create a blank image
img = np.zeros((600, 800, 3), dtype=np.uint8)

# Define cube vertices (projected to 2D)
cube = np.array([[50, 50], [150, 50], [150, 150], [50, 150], [70, 70], [170, 70], [170, 170], [70, 170]])

# Transformations
def translate(pts, tx, ty):
    return pts + [tx, ty]

def rotate(pts, angle):
    rad = np.radians(angle)
    center = np.mean(pts, axis=0)
    rotation_matrix = np.array([[np.cos(rad), -np.sin(rad)], [np.sin(rad), np.cos(rad)]])
    return (pts - center) @ rotation_matrix + center

def scale(pts, sx, sy):
    center = np.mean(pts, axis=0)
    return (pts - center) * [sx, sy] + center

# Function to draw the cube
def draw_cube(img, pts, color):
    # Define the edges of the cube
    edges = [
        (0, 1), (1, 2), (2, 3), (3, 0),  # Bottom square
        (4, 5), (5, 6), (6, 7), (7, 4),  # Top square
        (0, 4), (1, 5), (2, 6), (3, 7)   # Connecting lines
    ]
    for edge in edges:
        pt1 = tuple(pts[edge[0]].astype(int))
        pt2 = tuple(pts[edge[1]].astype(int))
        cv2.line(img, pt1, pt2, color, 2)

# Apply transformations
original_cube = cube
translated_cube = translate(cube, 300, 0)
rotated_cube = rotate(translate(cube, 0, 300), 45)
scaled_cube = scale(translate(cube, 300, 300), 1.5, 1.5)

# Draw the transformed cubes on the canvas
draw_cube(img, original_cube, (255, 0, 0))  # Original in the top-left corner
draw_cube(img, translated_cube, (0, 255, 0))  # Translated in the top-right corner
draw_cube(img, rotated_cube, (0, 0, 255))  # Rotated in the bottom-left corner
draw_cube(img, scaled_cube, (255, 255, 0))  # Scaled in the bottom-right corner

# Display the image
cv2.imshow("Geometric Transformations", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
