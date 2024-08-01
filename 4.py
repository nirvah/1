import cv2
import numpy as np

# Create a blank canvas
canvas = np.ones((500, 500, 3), dtype=np.uint8) * 255

# Define the initial object (a square)
obj_points = np.array([[100, 100], [200, 100], [200, 200], [100, 200]], dtype=np.int32)

# Define transformation matrices
translation_matrix = np.float32([[1, 0, 100], [0, 1, 50]])
rotation_matrix = cv2.getRotationMatrix2D((150, 150), 45, 1) 
scaling_matrix = np.float32([[1.5, 0, 0], [0, 1.5, 0]])

# Apply transformations
def transform_points(points, matrix):
    return np.array([np.dot(matrix, [x, y, 1])[:2] for x, y in points], dtype=np.int32)

translated_obj = transform_points(obj_points, translation_matrix)
rotated_obj = transform_points(translated_obj, rotation_matrix)
scaled_obj = transform_points(rotated_obj, scaling_matrix)

# Draw the objects on the canvas
for pts, color in zip([obj_points, translated_obj, rotated_obj, scaled_obj], [(0, 0, 0), (0, 255, 0), (255, 0, 0), (0, 0, 255)]):
    cv2.polylines(canvas, [pts], True, color, 2)

# Display the canvas
cv2.imshow("2D Transformations", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
