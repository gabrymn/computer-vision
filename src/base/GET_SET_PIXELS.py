import argparse
import cv2

#BGR - RGB
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the img")
args = vars(ap.parse_args())

image = cv2.imread(args['image'], cv2.IMREAD_COLOR)

cv2.imshow("Original", image)
cv2.waitKey()

x = 0
y = 0

(b, g, r) = image(y, x)

print("Pixel value at ({}, {}) - Red: {}, Green: {}, Blue: {}".format(x, y, r, g, b))

image[0, 0] = (0, 0, 255)
(b, g, r) = image[y, x]

x1 = 0
x2 = 100
y1 = 0
y2 = 100

top_left_crop = image[y1:y2, x1:x2]
cv2.imshow("Top Left Crop", top_left_crop)
cv2.waitKey()

image[y1:y2, x1:x2] = (255, 0, 0)
cv2.imshow("Updated", image)
cv2.waitKey()