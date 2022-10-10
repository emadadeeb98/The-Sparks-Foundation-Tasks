import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread("mandalas.jpg")
#plt.imshow(img)
#plt.show()
# by default openCV converts the image from RGB represntation of the
# pixels to BGR, so we need to convert it back to RGB
img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# plt.imshow(img_RGB)
# plt.show()
# Now we have to get the HSV represntatio of the image
img_HSV = cv2.cvtColor(img_RGB, cv2.COLOR_RGB2HSV)

# HSV Range for YELLOW colour: lower_yellow = [25,150,50] , upper_yellow = [35,255,255]
# we represent these ranges using numPY.

lower_yellow = np.array([25,150,50])
upper_yellow = np.array([35,255,255])

# Now we creat the mask to extract the YELLOW color from the given image
# we will be applying this mask to the HSV represntation of the image

mask = cv2.inRange(img_HSV, lower_yellow, upper_yellow)

# if we try to plot the previous mask the result won't be exactly yellow,
# we must do bitwisre_and to get the desired result

res = cv2.bitwise_and(img_RGB, img_RGB, mask = mask)

# plotting results:
rows = 1
columns = 2

# create figure
fig = plt.figure(figsize=(7, 4))

# setting values to rows and column variables
rows = 1
columns = 2

# Adds a subplot at the 1st position
fig.add_subplot(rows, columns, 1)

# showing image
plt.imshow(img_RGB)
plt.axis('off')
plt.title("First")

# Adds a subplot at the 2nd position
fig.add_subplot(rows, columns, 2)

# showing image
plt.imshow(res)
plt.axis('off')
plt.title("processed")

plt.show()