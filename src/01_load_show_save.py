import argparse
import cv2

#BGR - RGB

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the img")
args = vars(ap.parse_args())

# cv2.IMREAD_COLOR
image = cv2.imread(args["image"], cv2.IMREAD_GRAYSCALE)

print("image.shape: {}".format(image.shape))
print("image.shape: {}".format(image.dtype))
print("width: {}".format(image.shape[1]))
print("height: {}".format(image.shape[0]))

cv2.imshow("image", image)
cv2.waitKey()

cv2.imwrite("../out/01_img.jpg", image)