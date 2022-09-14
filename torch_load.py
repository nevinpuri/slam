import numpy as np
import cv2 as cv
import torch
from fastseg import MobileV3Small
from fastseg.image import colorize

cap = cv.VideoCapture("0.hevc")
model = MobileV3Small(num_classes=3, use_aspp=True)
state_dict = torch.load("/home/nevin/Desktop/model.pth")
model.from_pretrained("/home/nevin/Desktop/model.pth")
# model.load_state_dict(state_dict)
model.cuda()
model.eval()

# model = MobileV3Small.from_pretrained("/home/nevin/Desktop/model.pt")


while True:
    ret, frame = cap.read()

    if ret != True:
        break

    pred = model.predict_one(np.asarray(frame))
    # pred = model.predict_one(np.asarray(frame))
    count = np.count_nonzero(pred == 1)
    print(count)
    colorized = colorize(pred)
    cv.imshow("frame1", frame)
    cv.imshow("frame", np.asarray(colorized))

    key = cv.waitKey()

    if key == 113:
        quit()
