import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os

# set img and frame size
shape_img = [640,480]

cap = cv2.VideoCapture(0)
# set wid frame
cap.set(3, shape_img[0]) 
#set hig frame
cap.set(4, shape_img[1])
# cap.set(cv2.CAP_PROP_FPS, 60)

segmentor = SelfiSegmentation()
# show fps
fpsReader = cvzone.FPS()

# Get name img from folder Img_BackGround
listImg = os.listdir("Img_BackGround")

# create list_img_Background
imgList = []
for imgPath in listImg:
    img = cv2.imread(f'Img_BackGround/{imgPath}')
    img = cv2.resize(img,(shape_img[0],shape_img[1]))
    imgList.append(img)

indexImg = 0

while True:
    success, img = cap.read()

    # Remove BG and replace with img_BG.
    imgOut = segmentor.removeBG(img, imgList[indexImg], threshold=0.8)

    # Create photo frame with "2" column and scale 1:1
    imgStack = cvzone.stackImages([img, imgOut], 2,1)

    # display fps on the picture 
    _, imgStack = fpsReader.update(imgStack)

    print(indexImg)
    # Show frame image 
    cv2.imshow("image", imgStack)

    # switch between image background
    key = cv2.waitKey(1)
    if key == ord('a'):
        if indexImg>0:
            indexImg -=1
    elif key == ord('d'):
        if indexImg<len(imgList)-1:
            indexImg +=1
    elif key == ord('q'):
        break
