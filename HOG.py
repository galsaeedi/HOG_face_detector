
# import the necessary packages
import dlib
import argparse
import cv2

# construct the argument parser and parse the arguments
arg = argparse.ArgumentParser()
arg.add_argument("-i", "--image", required=True)
args = vars(arg.parse_args())


# load the input test image and convert it from BGR to RGB
image = cv2.imread(args["image"])
if image is None :
    print("No image !")
    exit()

hog= dlib.get_frontal_face_detector()
boxes = hog(image, 1)

############################## drow the rectangle with name in face ##############################
# loop over the recognized faces
for box in boxes:
    # draw rectangle on faces
    left = box.left()
    top = box.top()
    right = box.right() - left
    bottom = box.bottom() - top
    cv2.rectangle(image, (left,top),(left+right, top+bottom), (0, 255, 0), 2)


# show the output image
cv2.imshow("Image", image)
cv2.waitKey(0)
