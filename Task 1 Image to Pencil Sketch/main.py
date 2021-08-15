
import cv2
image = cv2.imread("test.jpg")
cv2.imshow("result", image)
cv2.waitKey(0)

gray= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Messi gray",gray)
cv2.waitKey(0)

inverted= 255 - gray
cv2.imshow("Inverted", inverted)
cv2.waitKey(0)


blurred = cv2.GaussianBlur(inverted, (21, 21), 0)
cv2.imshow("Blurred", blurred)
cv2.waitKey(0)

invertblurred = 255 - blurred
pencil = cv2.divide(gray, invertblurred, scale=256.0)
cv2.imshow("Sketch", pencil)
cv2.waitKey(0)