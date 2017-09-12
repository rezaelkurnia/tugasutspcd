import cv2

image = cv2.imread('E:\Wallpaper/panda.jpg')
grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('panda1.jpg', grey)
