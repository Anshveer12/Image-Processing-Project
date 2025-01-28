import cv2
import os

# File path to the .jfif image
file_path = r"C:\Users\vanshveer\Pictures\Saved Pictures\lion.jfif"

# Check if the file exists
if not os.path.exists(file_path):
    print("Error: File not found!")
else:
    # Attempt to load the image
    img = cv2.imread(file_path)
    if img is None:
        print("Error: Could not load the .jfif image. Check the file format or permissions.")
    else:
        print("Image loaded successfully.")

        # Resize the image to 1280x700 (width, height)
        img = cv2.resize(img, (1280, 700))

        # Display the image
        cv2.imshow("Original Image", img)
        cv2.waitKey(0)  # Wait for a key press
        cv2.destroyAllWindows()  # Close all OpenCV windows

print(img)

 

