#%%
import cv2

#%%
# The first argument is the image
image = cv2.imread(r"C:\Users\Shoaib Shaikh\Documents\OpenCV2\DD3Smoke.jpg")


#%%
#convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#%%
#blur it
blurred_image = cv2.GaussianBlur(image, (7,7), 0)

#%%
# Show both our images
cv2.imshow("Original image", image)
cv2.imshow("Blurred image", blurred_image)


#%%
# Run the Canny edge detector
canny = cv2.Canny(blurred_image, 320, 20)
cv2.imshow("Canny", canny)

#%%
contours, hierarchy= cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


#%%
print("Number of objects found = ", len(contours))


#%%
cv2.drawContours(image, contours, -1, (0,255,0), 2)
cv2.imshow("objects Found", image)
cv2.waitKey(0)
 

#%%
