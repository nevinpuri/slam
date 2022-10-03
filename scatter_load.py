import copy
import numpy as np
import cv2 as cv
import torch
from fastai.vision.all import load_learner
from fastseg import MobileV3Small


def pred(model, img):
    with torch.no_grad():
        img_tensor = img.transpose(2, 0, 1).astype("float32") / 255
        x_tensor = torch.from_numpy(img_tensor).to("cuda").unsqueeze(0)
        output = (
            torch.nn.functional.softmax(model.forward(x_tensor), dim=1).cpu().numpy()
        )

        return output


if __name__ == "__main__":
    model = MobileV3Small(num_classes=2, use_aspp=True)
    model.load_state_dict(torch.load("new_model.pt"))
    model.eval()
    print("done loading model")

    cap = cv.VideoCapture("0.hevc")
    while True:
        ret, frame = cap.read()

        if ret != True:
            break
