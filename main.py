import cv2
import numpy as np
import random

# List to store vertices coordinates
vertices = []


# Function to handle mouse events
def draw_triangle(event, x, y, flags, param):
    global vertices, image_copy

    if event == cv2.EVENT_LBUTTONDOWN:
        vertices.append((x, y))

        # Draw point
        cv2.circle(image_copy, (x, y), 3, (0, 0, 255), -1)

        if len(vertices) == 3:
            # Draw triangle with a random color
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            cv2.polylines(image_copy, [np.array(vertices)], isClosed=True, color=color, thickness=2)
            cv2.fillPoly(image_copy, [np.array(vertices)], color=color)
            # Reset vertices list for the next triangle
            vertices = []

    # Update image
    cv2.imshow('Image', image_copy)


# Image dimensions
width, height = 500, 500

# Create a blank image with a white background
image = np.ones((height, width, 3), dtype=np.uint8) * 255
image_copy = image.copy()

# Create a window and set a mouse callback function
cv2.namedWindow('Image')
cv2.setMouseCallback('Image', draw_triangle)

# Main loop
while True:
    cv2.imshow('Image', image_copy)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('s'):
        # Save the image to a file
        cv2.imwrite('triangles.png', image_copy)
        print("Image saved to triangles.png")
    elif key == 27:  # Esc key to exit
        break

cv2.destroyAllWindows()
