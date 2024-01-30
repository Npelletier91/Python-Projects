import cv2

im_path = 'Darwina.png'
image = cv2.imread(im_path)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Original image', image)
cv2.imshow('Grayscale image', gray_image)

# Wait for a key press and then close the displayed images
cv2.waitKey(0)
cv2.destroyAllWindows()


gray_path = 'Darwina_gray_scale.png'
cv2.imwrite(gray_path, gray_image)


result = cv2.imwrite(gray_path, gray_image)
if result:
    print("Image saved successfully.")
else:
    print("Error in saving image.")