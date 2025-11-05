import cv2
import numpy as np

# Function to find squares in the image
def find_squares(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_gray, (5, 5), 0)
    img_thresh = cv2.adaptiveThreshold(img_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    edges = cv2.Canny(img_thresh, 50, 150)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    squares = []
    for contour in contours:
        epsilon = 0.1 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        if (len(approx) == 4 or len(approx) == 1) and cv2.isContourConvex(approx):
            area = cv2.contourArea(approx)
            if area > 500:
                x, y, w, h = cv2.boundingRect(contour)
                aspect_ratio = w / h
                if 0.7 <= aspect_ratio <= 1.3:
                    squares.append((x, y, x + w, y + h))
    return squares

# Load the image
image_path = "C://Users//nehal//Downloads//WhatsApp Image 2024-01-21 at 11.11.37 AM.jpeg"
img = cv2.imread(image_path)

if img is None:
    print("Error: Could not read image.")
    exit()

# Find squares in the image
detected_squares = find_squares(img)
all_squares = detected_squares

# If you want to save the coordinates of the first five squares
a, b, c, d, e = all_squares[:5]

# Display the image with rectangles drawn around the squares
for square in detected_squares:
    x1, y1, x2, y2 = square
    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

# Annotate the image with the coordinates of square A
x1, y1, x2, y2 = a
cv2.putText(img, "A", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2, cv2.LINE_AA)

# Display the image
cv2.imshow('Detected Squares', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Print the coordinates of the first five squares
print("Coordinates of the first five squares:")
print("Square A:", a)
print("Square B:", b)
print("Square C:", c)
print("Square D:", d)
print("Square E:", e)