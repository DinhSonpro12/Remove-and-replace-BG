## cài đặt các thư viện 
# pip install cvzone
# pip install mediapipe


import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation

# # ảnh background
img_bg = ..........

# ảnh người cần thay thế bg
img_persion = .........

# # resize 1 ảnh về cùng 1 kích thước
img_bg = cv2.resize((400,400),img_bg)
img_persion = cv2.resize((400,400),img_persion)


segmentor = SelfiSegmentation()

imgOut = segmentor.removeBG(img_persion, img_bg, threshold=0.8)