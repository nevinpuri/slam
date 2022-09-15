import numpy as np
import cv2 as cv
import torch
from fastseg import MobileV3Small
from fastseg.image import colorize, blend
from PIL import Image

cap = cv.VideoCapture("2.hevc")
model = MobileV3Small.from_pretrained()
# state_dict = torch.load("/home/nevin/Desktop/model.pth")
# model.from_pretrained("/home/nevin/Desktop/model.pth")
# model.load_state_dict(state_dict)
model.cuda()
model.eval()

# # model = MobileV3Small.from_pretrained("/home/nevin/Desktop/model.pt")
# img = cv.imread(
#     "/home/nevin/Downloads/68747470733a2f2f692e696d6775722e636f6d2f4d4a4137564d4e2e706e67.png"
# )

# pred = model.predict_one(np.asarray(img))
# pred = colorize(pred)

# cv.imshow("frame2", np.asarray(pred))

# cv.waitKey()


while True:
    ret, frame = cap.read()

    if ret != True:
        break

    print(frame.shape)

    pred = model.predict_one(np.asarray(frame))

    # pred = model.predict_one(np.asarray(frame))
    # count = np.count_nonzero(pred == 1)
    colorized = colorize(pred)
    cv.imshow("frame1", frame)
    cv.imshow("frame", np.asarray(colorized))

    key = cv.waitKey()

    if key == 113:
        quit()
