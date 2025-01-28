import cv2

# Image conversion project: Convert a colored image to grayscale
path = input("Enter the path and name of an image: ")
print("You entered this:", path)

# Reads the image from the specified path in grayscale mode (0 indicates grayscale)
img1 = cv2.imread(path, 0)
if img1 is None:
    print("Error: Image not found. Please check the path and try again.")
else:
    img1 = cv2.resize(img1, (560, 700))  # Resizes the image to 560x700
    img1 = cv2.flip(img1, 0)  # Flips the image vertically (0 means vertical flip)
    
    # Displays the processed grayscale image
    cv2.imshow("Converted Image", img1)
    
    # Waits for the user to press a key
    k = cv2.waitKey(0)  # Waits indefinitely for a key press
    
    if k == ord("s"):  # If the user presses 's', save the image
        cv2.imwrite("output.png", img1)  # Save the processed image as output.png
        print("Image saved as 'output.png'")
    else:
        cv2.destroyAllWindows()  # Closes all OpenCV windows if any other key is pressed
