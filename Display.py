#%%
import cv2

#%%
# The first argument is the image
image = cv2.imread(r'C:\Users\Shoaib Shaikh\Documents\OpenCV2\untitled.png')


#%%
#convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#%%
#blur it
blurred_image = cv2.GaussianBlur(image, (7,7), 0)

#%%
cv2.imshow("Original Image", image)


#%%
canny = cv2.Canny(blurred_image, 10, 30)
cv2.imshow("Canny with low thresholds", canny)

#%%
canny2 = cv2.Canny(blurred_image, 50, 150)
cv2.imshow("Canny with high thresholds", canny2)

cv2.waitKey(0)

#%%
