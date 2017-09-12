import cv2

image = cv2.imread('E:\Wallpaper/mobil.jpg')
cv2.normalize(image, image, alpha=30, beta=250, norm_type=cv2.NORM_MINMAX)
cv2.imwrite('mobilContrastStretching.jpg', image)


