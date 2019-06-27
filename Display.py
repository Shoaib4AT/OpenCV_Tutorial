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
# Show all 3 images
cv2.imshow("Original Image", image)
cv2.imshow("Gray Image", gray_image)
cv2.imshow("Blurred Image", blurred_image)
 
cv2.waitKey(0)

