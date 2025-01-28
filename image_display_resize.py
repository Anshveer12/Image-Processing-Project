import cv2
img1 = cv2.imread(r"C:\Users\vanshveer\Pictures\Saved Pictures\lion.jfif",1)
img1 = cv2.resize(img1,(1200,700))#width ,height
print(img1)
cv2.imshow("original",img1)

#cv2.IMREAD_GRAYSCALE : Loads image in grayscale
img2 = cv2.imread(r"C:\Users\vanshveer\Pictures\Saved Pictures\lion.jfif",0)
img2 = cv2.resize(img2,(1200,700))#width ,height
cv2.imshow("Gray Scale Image",img2)
print("Image in gray scale==\n",img2)

cv2.waitKey()
cv2.destroyAllWindows()
