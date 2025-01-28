import cv2
#Now capture video from webcam and save into memory
# external webcam=1,laptop camera=0
cap = cv2.VideoCapture(0)

#DIVX, XVID, MJPG, X264, WMV1, WMV2
fourcc = cv2.VideoWriter_fourcc(*"XVID") #"XVID
output_folder = r"C:\Users\vanshveer\Desktop\Image Processing\output"
#It contains four parameter, name , codec, fps, resolution
output = cv2.VideoWriter(output_folder + r"\output.avi", fourcc, 20.0, (640, 480))



print(cap)

while cap.isOpened():
    ret,frame = cap.read()
    if ret == True:
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame",frame)
        cv2.imshow("gray",gray)
        output.write(frame)
        k = cv2.waitKey(5)
        if k == ord("q"):
            break
cap.release()
output.release()
cv2.destroyAllWindows()  